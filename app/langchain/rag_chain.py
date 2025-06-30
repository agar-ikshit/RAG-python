from qdrant_client.http.models import Distance, VectorParams
from qdrant_client import QdrantClient

from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain

from app.core.embeddings import get_embedding_model
from app.db.vector_store import get_qdrant_client
from app.langchain.memory import get_memory
from app.core.embeddings import get_embedding_model
from app.db.vector_store import ensure_collection  

import os
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")


def get_vectorstore():
    qdrant_client = get_qdrant_client()
    embedding_fn = get_embedding_model()

    
    ensure_collection()

    return QdrantVectorStore(
        client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embedding=embedding_fn
    )



# Step 1: Custom Prompt


CUSTOM_PROMPT_TEMPLATE = """You are a helpful and knowledgeable AI assistant representing Logicspice. Your goal is to understand the user's question clearly and provide accurate, insightful, and complete answers.

When relevant, recommend suitable Logicspice software products or services as practical solutions, including key features and pricing. Suggestions should feel natural and genuinely helpful — avoid sounding promotional.

Use the provided context if available, but rely on your general knowledge when needed to ensure a comprehensive response. Always maintain a professional, friendly tone.

Context:
{context}

User Question:
{question}

Answer:


"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=CUSTOM_PROMPT_TEMPLATE
)


# Step 2: Initialize Vectorstore


def get_vectorstore():
    qdrant_client = get_qdrant_client()
    embedding_fn = get_embedding_model()

    return QdrantVectorStore(
        client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embedding=embedding_fn
    )


# Step 3: Build RAG Chain


def get_rag_chain(user_id: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=1
    )
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    memory = get_memory(user_id)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer", 
        combine_docs_chain_kwargs={"prompt": prompt},
    )
    return chain
    embedding_fn = get_embedding_model()