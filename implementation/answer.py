"""Agentic RAG for HMAS (Holland Marine Assistant System).

Unlike a classic RAG (which always injects the retrieved context), here the LLM
is an *agent* that decides when to call the `search_documentation` tool to look
up the technical manuals, using the OpenAI Agents SDK.
"""

import os
import time

import chromadb
from agents import Agent, Runner, function_tool
from chromadb.utils import embedding_functions

from implementation.config import (
    COLLECTION_NAME,
    COMPANY_NAME,
    DB_PATH,
    EMBEDDING_MODEL,
    HMAS_SYSTEM_PROMPT,
    MODEL,
    RETRIEVAL_K,
)

# Same embedding function as ingest.py (text-embedding-3-small).
_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"), model_name=EMBEDDING_MODEL
)
_collection = None  # lazy cache


def _get_collection():
    """Open the persisted collection. Raise a clear error if ingest is missing."""
    global _collection
    if _collection is None:
        if not DB_PATH.exists():
            raise RuntimeError(
                f"Vector store not found at {DB_PATH}. "
                f"Run first: uv run python -m implementation.ingest"
            )
        client = chromadb.PersistentClient(path=str(DB_PATH))
        _collection = client.get_collection(COLLECTION_NAME, embedding_function=_ef)
    return _collection


def _query_with_retry(consulta: str, attempts: int = 3):
    """Query the collection, retrying on transient errors.

    Each query embeds the text via the OpenAI embeddings API; a single network
    blip or rate-limit there would otherwise raise and make the agent report a
    spurious "technical problem". Retry with a short backoff before giving up.
    """
    last_err: Exception | None = None
    for i in range(attempts):
        try:
            return _get_collection().query(query_texts=[consulta], n_results=RETRIEVAL_K)
        except Exception as e:  # transient embedding/API/network error
            last_err = e
            time.sleep(0.8 * (i + 1))
    raise last_err


# @function_tool turns the function into a tool the agent can invoke.
# The docstring is what the LLM reads to decide when and how to call it.
@function_tool
def search_documentation(query: str) -> str:
    """Search the Holland Marine technical documentation (engineering guides,
    installation, operator and maintenance manuals).

    Use it to answer any technical question about vessel systems: configuration,
    troubleshooting, installation, channel setup, alarm management, network
    configuration, hardware identification and parameter settings. The query
    should describe what you are looking for, e.g. 'basic network layout for the
    operator work station'. Returns documentation fragments; each block starts
    with '### <document name> — Section <number> <title>', which you must use to
    cite the source.
    """
    results = _query_with_retry(query)
    docs, metas = results["documents"][0], results["metadatas"][0]
    if not docs:
        return "No information was found in the documentation for that query."
    blocks = [
        f"### {meta['documento']} — Section {meta['seccion']}\n{doc}"
        for doc, meta in zip(docs, metas)
    ]
    return "\n\n---\n\n".join(blocks)


agent = Agent(
    name=f"{COMPANY_NAME} Assistant (HMAS)",
    instructions=HMAS_SYSTEM_PROMPT,
    tools=[search_documentation],
    model=MODEL,
)


def _text(content) -> str:
    """Normalise a message's content to a plain string.

    Gradio may deliver content as a string or as a list of parts
    (e.g. [{"type": "text", "text": "..."}]); the Responses API only accepts
    role/content with a string, so we flatten it.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            (p.get("text") or p.get("content") or "") if isinstance(p, dict) else str(p)
            for p in content
        )
    return str(content)


def answer_question(question: str, history: list[dict] | None = None) -> str:
    """Answer a technical question, grounded in the retrieved documentation.

    The agent decides on its own when to call search_documentation.
    Runner.run_sync runs the tool loop automatically until the final answer.
    """
    history = history or []
    # Gradio's Chatbot adds extra keys (options, metadata) and sometimes delivers
    # content as a list of parts; sanitise to plain role + content (string).
    messages = [{"role": m["role"], "content": _text(m["content"])} for m in history]
    messages.append({"role": "user", "content": question})
    result = Runner.run_sync(agent, messages)
    return result.final_output
