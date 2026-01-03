from __future__ import annotations

from pathlib import Path
from typing import List

import chromadb
from sentence_transformers import SentenceTransformer

from common.ollama_client import generate

TEMPLATE = Path(__file__).parent / "rag_prompt_insecure.txt"
DB_DIR = Path(__file__).parents[1] / "../security/rag/chroma_db"
COLLECTION = "security_docs"

def retrieve(query: str, k: int = 2) -> List[str]:
    client = chromadb.PersistentClient(path=str(DB_DIR))
    col = client.get_or_create_collection(COLLECTION)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    qemb = model.encode([query]).tolist()
    res = col.query(query_embeddings=qemb, n_results=k)
    return res["documents"][0] if res.get("documents") else []

def main() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    print("Prompted RAG Runner. Type 'exit' to quit.\n")
    while True:
        q = input("Question: ").strip()
        if q.lower() in {"exit","quit"}:
            break
        ctx_docs = retrieve(q)
        ctx = "\n\n---\n\n".join(ctx_docs)
        prompt = template.replace("{{CONTEXT}}", ctx).replace("{{QUESTION}}", q)
        out = generate(prompt, temperature=0.2, num_predict=380)
        print(f"\nAnswer:\n{out}\n")

if __name__ == "__main__":
    main()
