import os
import streamlit as st
from dotenv import load_dotenv

# LangSmith toggles via env

def _apply_langsmith(enabled: bool):
    if enabled:
        os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
        os.environ.setdefault("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
    else:
        os.environ["LANGCHAIN_TRACING_V2"] = "false"


# Charger .env très tôt
load_dotenv()

from agentic_rag import run_query  # noqa: E402
from rag_indexer import build_or_load_faiss, DEFAULT_INDEX_DIR, DEFAULT_DATA_DIR  # noqa: E402

st.set_page_config(page_title="Agentic RAG – Groq + FAISS + Tavily", layout="wide")

st.title("🤖 Agentic RAG – Groq + FAISS + Tavily")

with st.sidebar:
    st.header("⚙️ Paramètres")

    # État des clés
    has_groq = bool(os.getenv("GROQ_API_KEY", "").strip())
    has_tavily = bool(os.getenv("TAVILY_API_KEY", "").strip())

    st.write("**Clés détectées**:")
    st.checkbox("GROQ_API_KEY", value=has_groq, disabled=True)
    st.checkbox("TAVILY_API_KEY", value=has_tavily, disabled=True)

    enable_web = st.toggle("Activer Tavily (web search)", value=has_tavily)
    enable_tracing = st.toggle("Activer LangSmith (tracing)", value=os.getenv("LANGCHAIN_TRACING_V2", "false").lower()=="true")
    _apply_langsmith(enable_tracing)

    k = st.slider("k – passages récupérés", min_value=2, max_value=8, value=4)

    st.divider()
    if st.button("🔁 (Re)construire l'index FAISS"):
        # Supprime le dossier d'index pour forcer la reconstruction
        for p in DEFAULT_INDEX_DIR.rglob("*"):
            try:
                p.unlink()
            except IsADirectoryError:
                pass
        try:
            vs, _ = build_or_load_faiss(DEFAULT_INDEX_DIR, DEFAULT_DATA_DIR)
            st.success("Index reconstruit ✅")
        except Exception as e:
            st.error(f"Erreur reconstruction index: {e}")

st.caption("Ajoutez vos documents (.txt/.md/.pdf) dans le dossier `data/` puis reconstruisez l'index si nécessaire.")

query = st.text_area("Votre question", placeholder="Ex: Résume le contenu clé de mes documents et complète avec l'actualité récente.", height=120)

col1, col2 = st.columns([1,1])
with col1:
    if st.button("Envoyer", type="primary"):
        if not query.strip():
            st.warning("Veuillez saisir une question.")
        elif not os.getenv("GROQ_API_KEY", "").strip():
            st.error("Configurez d'abord GROQ_API_KEY dans votre .env")
        else:
            with st.spinner("L'agent réfléchit…"):
                try:
                    out = run_query(query, k=k, enable_web=enable_web)
                    st.subheader("Réponse")
                    st.write(out["answer"])  # texte principal

                    if out.get("web_complement"):
                        st.subheader("Complément web")
                        st.write(out["web_complement"])  # résumé / citations outil

                    sources = out.get("sources") or []
                    if sources:
                        st.subheader("Sources")
                        for s in sources:
                            st.write(f"• {s}")
                except Exception as e:
                    st.error(f"Erreur: {e}")

with col2:
    st.subheader("Notebook agentic_rag.ipynb (aperçu texte)")
    nb_path = "agentic_rag.ipynb"
    if os.path.exists(nb_path):
        try:
            with open(nb_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            st.code(content[:20000] + ("\n… (tronqué)" if len(content)>20000 else ""), language="json")
        except Exception as e:
            st.info(f"Impossible d'afficher le notebook: {e}")
    else:
        st.info("Aucun notebook trouvé. (Optionnel) Créez `agentic_rag.ipynb` pour vos explorations.")