from __future__ import annotations
import os
from pathlib import Path
from typing import List

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from bs4 import BeautifulSoup

DEFAULT_DATA_DIR = Path("data")
DEFAULT_INDEX_DIR = Path("indexes/faiss")


def _ensure_dirs():
    DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    DEFAULT_INDEX_DIR.mkdir(parents=True, exist_ok=True)


def load_documents(data_dir: Path = DEFAULT_DATA_DIR):
    """Charge .txt, .md, .pdf depuis data_dir. Nettoie rapidement le HTML si présent."""
    _ensure_dirs()
    docs = []

    # .txt et .md
    for ext in ("**/*.txt", "**/*.md"):
        loader = DirectoryLoader(str(data_dir), glob=ext, loader_cls=TextLoader, show_progress=True, use_multithreading=True)
        docs += loader.load()

    # .pdf
    for pdf_path in data_dir.rglob("*.pdf"):
        loader = PyPDFLoader(str(pdf_path))
        docs += loader.load()

    # Nettoyage HTML brut si jamais on a du contenu avec balises
    cleaner = Html2TextTransformer()
    docs = cleaner.transform_documents(docs)

    # Fallback de démonstration si aucun doc
    if not docs:
        from langchain_core.documents import Document
        demo = (
            "Ce dépôt démontre un pipeline Agentic RAG avec FAISS (index local), "
            "Tavily (recherche web) et Groq (LLM Llama3). Ajoutez vos PDF/TXT/MD dans ./data."
        )
        docs = [Document(page_content=demo, metadata={"source": "demo"})]

    return docs


def build_or_load_faiss(index_dir: Path = DEFAULT_INDEX_DIR, data_dir: Path = DEFAULT_DATA_DIR):
    """Construit l'index FAISS s'il n'existe pas, sinon le recharge."""
    _ensure_dirs()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index_file = index_dir / "index.faiss"

    if any(index_dir.iterdir()):
        # Chargement
        vs = FAISS.load_local(str(index_dir), embeddings, allow_dangerous_deserialization=True)
        return vs, embeddings

    # Construction
    docs = load_documents(data_dir)
    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(str(index_dir))
    return vs, embeddings