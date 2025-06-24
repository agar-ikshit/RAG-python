

from app.core.embeddings import embed_texts
from app.db.vector_store import upsert_embeddings
from data import chunks_fiverclone  # You can import all your other product chunks similarly

def embed_and_store_all():
    all_chunks = chunks_fiverclone  # + other chunk lists
    texts = [chunk["content"] for chunk in all_chunks]
    metadatas = [chunk["metadata"] for chunk in all_chunks]

    embeddings = embed_texts(texts)
    upsert_embeddings(embeddings, metadatas)
