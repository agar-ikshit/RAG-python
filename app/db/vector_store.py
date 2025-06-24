from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

collection_name = "logicspice_products"


def ensure_collection():
    collections = client.get_collections().collections
    if collection_name not in [col.name for col in collections]:
        print(f"Creating collection: {collection_name}")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )
    else:
        print(f"Collection already exists: {collection_name}")


def upsert_embeddings(vectors, metadatas):
    ensure_collection()

    points = []
    for idx, (embedding, metadata) in enumerate(zip(vectors, metadatas)):
        points.append({
            "id": idx,
            "vector": embedding,
            "payload": {
                **metadata,
                "page_content": metadata["content"]  
            }
        })

    client.upsert(
        collection_name=collection_name,
        points=points
    )


def get_qdrant_client():
    return client


if __name__ == "__main__":
    print(client.get_collections())
