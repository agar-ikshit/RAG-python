import json
from app.core.embeddings import embed_texts
from app.db.vector_store import ensure_collection, upsert_embeddings
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "logicspice_products")
VECTOR_SIZE = 768  

# Load chunks
with open("logicspice_chunks.jsonl", "r") as f:
    data = [json.loads(line) for line in f.readlines()]

texts = [item["content"] for item in data]
metadatas = []
for item in data:
    metadata = item.get("metadata", {})
    metadata["content"] = item.get("content", "")
    metadatas.append(metadata)

embeddings = embed_texts(texts)

upsert_embeddings(embeddings, metadatas)

print("Upload complete.")
