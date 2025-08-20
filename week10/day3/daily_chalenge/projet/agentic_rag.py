from __future__ import annotations
import os
from typing import Dict, Any, List

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain_core.documents import Document

from rag_indexer import build_or_load_faiss, DEFAULT_INDEX_DIR


# ——— LLM (Groq)

def get_llm() -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GROQ_API_KEY manquant dans l'environnement.")

    # Modèles Groq courants : "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"
    model = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    return ChatGroq(
        groq_api_key=api_key,
        model=model,
        temperature=0.2,
        max_tokens=1024,
    )


# ——— Tools (Tavily)

def get_tools() -> List[Any]:
    tools: List[Any] = []
    tavily_key = os.getenv("TAVILY_API_KEY", "").strip()
    if tavily_key:
        tools.append(TavilySearchResults(api_key=tavily_key, k=4))
    return tools


# ——— RAG Chain

def get_rag_chain(k: int = 4):
    vs, _ = build_or_load_faiss(DEFAULT_INDEX_DIR)
    retriever = vs.as_retriever(search_kwargs={"k": k})
    qa = RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
    )
    return qa


# ——— Agent combinant RAG + Tools Web

def get_agent_with_tools():
    tools = get_tools()
    if not tools:
        return None
    agent = initialize_agent(
        tools=tools,
        llm=get_llm(),
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=False,
        handle_parsing_errors=True,
    )
    return agent


def _format_sources(docs: List[Document]) -> List[str]:
    sources = []
    for d in docs:
        src = d.metadata.get("source") or d.metadata.get("file_path") or "inconnu"
        page = d.metadata.get("page")
        if page is not None:
            sources.append(f"{src}#page={page}")
        else:
            sources.append(str(src))
    # Uniques en gardant l'ordre
    seen = set()
    uniq = []
    for s in sources:
        if s not in seen:
            uniq.append(s)
            seen.add(s)
    return uniq


def run_query(
    query: str,
    *,
    k: int = 4,
    enable_web: bool = True,
) -> Dict[str, Any]:
    """Exécute la boucle RAG puis (optionnel) la recherche web.

    Retourne un dict {"answer", "sources", "web_complement"}.
    """
    qa = get_rag_chain(k=k)
    rag_out = qa({"query": query})

    answer = rag_out.get("result", "")
    src_docs: List[Document] = rag_out.get("source_documents", []) or []
    sources = _format_sources(src_docs)

    web_complement = None
    if enable_web and get_tools():
        try:
            agent = get_agent_with_tools()
            web_complement = agent.run(query)
        except Exception as e:
            web_complement = f"Erreur outil web: {e}"

    return {
        "answer": answer,
        "sources": sources,
        "web_complement": web_complement,
    }