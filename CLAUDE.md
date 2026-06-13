# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync

# (Re)build the vector store from knowledge-base — run when the manuals change
uv run python -m implementation.ingest

# Run the app (auto-runs ingest on first launch if vector_db/ is missing)
uv run python app.py
```

## Environment variables

Copy `.env.example` to `.env` and fill in:

```
OPENAI_API_KEY=sk-...
MODEL=gpt-4o-mini                       # chat model (default if not set)
EMBEDDING_MODEL=text-embedding-3-small  # rerun ingest if you change this
RETRIEVAL_K=6                           # number of RAG chunks retrieved per query
```

## Architecture

**HMAS** (Holland Marine Assistant System) is an **agentic** RAG technical
assistant over the marine-vessel manuals in `knowledge-base/`. Logic lives in
the **`implementation/`** package; `app.py` is a thin Gradio UI on top.
Ingestion (build the vector store) is separated from answering (load it and
chat). Built on the **OpenAI Agents SDK** (`openai-agents`): instead of always
injecting retrieved context, the LLM is an agent that decides when to call the
`search_documentation` tool. Same RAG architecture as the sibling `Lori`
project, adapted for long-form technical manuals instead of single product
sheets.

### `implementation/` package

- **`config.py`** — single source of truth: paths (`KNOWLEDGE_BASE`, `DB_PATH`,
  `COLLECTION_NAME`), models (`MODEL`, `EMBEDDING_MODEL`), retrieval/chunking
  params (`RETRIEVAL_K`, `CHUNK_SIZE=900`, `CHUNK_OVERLAP=200`),
  `INGEST_EXCLUDE`, `COMPANY_NAME`, and the `HMAS_SYSTEM_PROMPT`. Most values
  are env-overridable.
- **`ingest.py`** — **section-aware** ingestion. `fetch_documents()` reads every
  `knowledge-base/**/*.md` (category = parent folder, document name = first
  non-numbered `# ` heading). `_parse_sections()` walks the Markdown headings
  and groups text under the nearest *real* numbered section; `_as_section()`
  rejects misformatted table-row headings (e.g. `## 2 GB 38.4 11`) by requiring
  a real word and no embedded decimal. `create_chunks()` splits each section
  body with a `RecursiveCharacterTextSplitter` and prefixes every fragment with
  `[Document: …] [Section: <number> <title>]`, attaching
  `{documento, seccion, categoria, fuente}` metadata so the assistant can cite
  "document name (section X.Y)". `create_embeddings()` recreates the ChromaDB
  collection (drops the old one) and persists it to `vector_db/`.
- **`answer.py`** — **agentic RAG**. Lazily opens the persisted collection
  (`_get_collection`, with a clear error if ingest hasn't run).
  `search_documentation(query)` is a `@function_tool` that queries the top
  `RETRIEVAL_K` chunks and returns them as
  `### <document> — Section <number> <title>` blocks (the agent cites that
  header). An `Agent` is defined with `HMAS_SYSTEM_PROMPT`,
  `tools=[search_documentation]`, `model=MODEL`. `answer_question(question,
  history)` runs `Runner.run_sync`, which loops tool calls automatically until
  the final answer. The prompt forces the agent to search first, answer only
  from retrieved docs, cite document+section, preserve safety/electrical
  warnings, and reply in the user's language.

### Knowledge source

- `knowledge-base/**/*.md` — technical manuals (engineering guides, installation,
  operator, maintenance), grouped into category folders (`automation`, …).
  Currently: the MEGA-GUARD Ship Automation Systems Engineering Guide.
  Embedded with OpenAI `text-embedding-3-small` via ChromaDB's
  `OpenAIEmbeddingFunction` — `ingest.py` and `answer.py` must use the same
  model or the persisted collection won't match.
- `raw_data/` — source PDFs and extracted images, **not** ingested (only
  `knowledge-base/` is). Working area for producing the Markdown manuals.

### Vector store

Persisted on disk under `vector_db/` (gitignored) by a
`chromadb.PersistentClient`. `app.py` runs `ingest.main()` automatically on
first launch when `vector_db/` is missing; thereafter it just loads it.

### `app.py` (Gradio UI)

Two-column layout: identity column (`scale=1`, optional `logo.png`) + chat
(`scale=4`) using a `type="messages"` `gr.Chatbot`. `respond()` calls
`answer_question` and appends the user/assistant turns to the history.
