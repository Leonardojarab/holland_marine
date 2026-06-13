"""Ingest the knowledge-base into the vector store.

Reads every technical manual (.md) under knowledge-base, splits it into
section-aware fragments with metadata (document, section, category, source)
and persists them into a ChromaDB collection on disk. Run whenever the
documents change:

    uv run python -m implementation.ingest

Unlike a flat product-sheet ingest, the splitter here is *section aware*: it
walks the Markdown headings, attaches the nearest real section number+title to
every fragment, and exposes it as metadata so the assistant can cite
"document name (section X.Y)" accurately.
"""

import os
import re

import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

from implementation.config import (
    CHUNK_OVERLAP,
    COLLECTION_NAME,
    DB_PATH,
    EMBEDDING_MODEL,
    INGEST_EXCLUDE,
    KNOWLEDGE_BASE,
    SECTION_MAX_CHARS,
)

# OpenAI embeddings (text-embedding-3-small). Requires OPENAI_API_KEY.
# Must be identical to answer.py so the persisted collection matches.
_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"), model_name=EMBEDDING_MODEL
)

# Recursive splitter, used ONLY to break up sections that exceed
# SECTION_MAX_CHARS. It tries to cut by paragraphs (\n\n), then lines (\n), then
# spaces and finally characters, respecting the Markdown structure better than a
# blind fixed-size cut. Sections within the limit are kept whole (see
# _section_pieces).
_splitter = RecursiveCharacterTextSplitter(
    chunk_size=SECTION_MAX_CHARS, chunk_overlap=CHUNK_OVERLAP
)

# A Markdown heading line of any level: captures the text after the '#'s.
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")

# A heading whose text is a numbered section: "3.8 Basic network layout",
# "2 ABOUT THIS MANUAL", "5.2.4 Program". Captures (number, title).
_SECTION_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(.+)$")

# A decimal number such as "38.4" — its presence in a "title" means the heading
# is really a misformatted table row ("## 2 GB 38.4 11"), not a section.
_DECIMAL_RE = re.compile(r"\d\.\d")

# At least one real word (3+ letters) — filters junk headings like "GB 30 11".
_WORD_RE = re.compile(r"[A-Za-z]{3,}")


def _heading_text(line: str) -> str | None:
    """Return the text of a Markdown heading, or None if the line isn't one."""
    m = _HEADING_RE.match(line)
    return m.group(1).strip() if m else None


def _as_section(heading: str) -> tuple[str, str] | None:
    """Parse a heading into (number, title) if it's a real numbered section.

    Rejects misformatted table rows ("2 GB 38.4 11") and number-only junk by
    requiring a real word and no embedded decimal.
    """
    m = _SECTION_RE.match(heading)
    if not m:
        return None
    number, title = m.group(1), m.group(2).strip()
    if _DECIMAL_RE.search(title) or not _WORD_RE.search(title):
        return None
    return number, title


def _document_title(text: str, fallback: str) -> str:
    """Document name: first non-numbered '# ' heading, or the filename."""
    for line in text.splitlines():
        h = _heading_text(line)
        if h is not None and _as_section(h) is None:
            return h
    return fallback


def _excluded(name: str) -> bool:
    """True if the file should be skipped (see INGEST_EXCLUDE)."""
    return any(p.lower() in name.lower() for p in INGEST_EXCLUDE)


def _parse_sections(text: str, doc_title: str) -> list[tuple[str, str]]:
    """Split the document into (section_label, body) blocks.

    Walks the lines accumulating text under the current section. A new section
    starts at every heading recognised by _as_section; other headings (and all
    body text) are kept as content. The leading material before the first
    numbered section is attached to the document title itself.
    """
    sections: list[tuple[str, str]] = []
    current_label = doc_title  # preface, before the first numbered section
    buf: list[str] = []
    for line in text.splitlines():
        h = _heading_text(line)
        if h is not None:
            sec = _as_section(h)
            if sec is not None:
                if buf:
                    sections.append((current_label, "\n".join(buf)))
                number, title = sec
                current_label = f"{number} {title}"
                buf = [h]  # keep the heading text in the section body for context
                continue
        buf.append(line)
    if buf:
        sections.append((current_label, "\n".join(buf)))
    return sections


def fetch_documents() -> list[dict]:
    """Read every .md manual under knowledge-base, skipping excluded files.

    The subfolder is the category (automation, ...) and the document name is
    derived from the first non-numbered heading.
    """
    documents = []
    for path in sorted(KNOWLEDGE_BASE.rglob("*.md")):
        if _excluded(path.name):
            print(f"[ingest] skipped (excluded): {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        documents.append(
            {
                "stem": path.stem,
                "categoria": path.parent.name,
                "documento": _document_title(text, path.stem),
                "text": text,
                "fuente": str(path.relative_to(KNOWLEDGE_BASE.parent)),
            }
        )
    return documents


def _section_pieces(body: str) -> list[str]:
    """Return the section as a single piece, splitting only if it is too long.

    Most sections fit within SECTION_MAX_CHARS and stay whole, so related facts
    are embedded together. Oversized sections are split *within* their own
    boundary so a chunk never mixes content from two different sections.
    """
    if len(body) <= SECTION_MAX_CHARS:
        return [body]
    return _splitter.split_text(body)


def create_chunks(documents: list[dict]) -> tuple[list[str], list[str], list[dict]]:
    """Split each manual into section-based chunks for retrieval.

    One chunk per section (oversized sections split within their boundary). Each
    chunk is prefixed with its document and section so that both the vector
    search and the LLM know where it comes from. Returns (docs, ids, metas).
    """
    docs: list[str] = []
    ids: list[str] = []
    metas: list[dict] = []
    for d in documents:
        for s_idx, (seccion, body) in enumerate(_parse_sections(d["text"], d["documento"])):
            for c_idx, chunk in enumerate(_section_pieces(body)):
                if not chunk.strip():
                    continue
                docs.append(
                    f"[Document: {d['documento']}] [Section: {seccion}]\n{chunk}"
                )
                ids.append(f"{d['stem']}-{s_idx}-{c_idx}")
                metas.append(
                    {
                        "documento": d["documento"],
                        "seccion": seccion,
                        "categoria": d["categoria"],
                        "fuente": d["fuente"],
                    }
                )
    return docs, ids, metas


def create_embeddings(docs: list[str], ids: list[str], metas: list[dict]) -> None:
    """Generate the embeddings and persist them into ChromaDB.

    Recreates the collection from scratch to avoid duplicates on re-ingest.
    """
    client = chromadb.PersistentClient(path=str(DB_PATH))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass  # Did not exist yet: first ingestion.

    collection = client.create_collection(COLLECTION_NAME, embedding_function=_ef)
    collection.add(documents=docs, ids=ids, metadatas=metas)

    n_docs = len({m["fuente"] for m in metas})
    print(f"[ingest] {n_docs} document(s) -> {collection.count()} fragments in {DB_PATH}")


def main() -> None:
    documents = fetch_documents()
    docs, ids, metas = create_chunks(documents)
    create_embeddings(docs, ids, metas)
    print("[ingest] Ingestion complete")


if __name__ == "__main__":
    main()
