import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        task_type="retrieval_document"
    )


def embed_texts(texts, batch_size=10):
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        try:
            responses = [
                genai.embed_content(
                    model="models/embedding-001",
                    content=text,
                    task_type="retrieval_document"
                ) for text in batch
            ]
            batch_embeddings = [r["embedding"] for r in responses]
            all_embeddings.extend(batch_embeddings)
        except Exception as e:
            print(f"Error embedding batch {i // batch_size + 1}: {e}")
            continue

    return all_embeddings

