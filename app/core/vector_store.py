from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os, tenacity, requests
from dotenv import load_dotenv
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HUGGINGFACEHUB_API_TOKEN not set")
 
@tenacity.retry(stop=tenacity.stop_after_attempt(3),
                wait=tenacity.wait_fixed(5),
                reraise=True)
def _embed_with_retry(texts: list[str]) -> list[list[float]]:
    """Call HF inference API directly and return vectors."""
    resp = requests.post(
        "https://api-inference.huggingface.co/models/BAAI/bge-base-en-v1.5",
        headers={"Authorization": f"Bearer {HF_TOKEN}",
                 "Content-Type": "application/json"},
        json={"inputs": texts},
        timeout=60
    )
    if resp.status_code != 200:
        raise RuntimeError(
            f"HuggingFace inference error {resp.status_code}: {resp.text[:300]}"
        )
    return resp.json()

class RobustHFEmbeddings(HuggingFaceInferenceAPIEmbeddings):
    """Same interface, but we bypass the buggy LC implementation."""
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return _embed_with_retry(texts)
    def embed_query(self, text: str) -> list[float]:
        return _embed_with_retry([text])[0]

embeddings = RobustHFEmbeddings(
    api_key=HF_TOKEN,
    model_name="BAAI/bge-base-en-v1.5"
)

# ------------------------------------------------------------------
# 2. Chroma instance
# ------------------------------------------------------------------
vectordb = Chroma(persist_directory="./chroma_db",
                  embedding_function=embeddings)

# ------------------------------------------------------------------
# 3. Public helpers
# ------------------------------------------------------------------
def index_documents(document_chunks: list[Document]):
    vectordb.add_documents(document_chunks)

def find_related_documents(query: str) -> list[Document]:
    return vectordb.similarity_search(query)

def clear_vector_store():
    pass