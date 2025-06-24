from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.embeddings import get_embedding_model
from app.db.vector_store import get_qdrant_client
from langchain_qdrant import QdrantVectorStore

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

qdrant = get_qdrant_client()
embedding = get_embedding_model()

vectorstore = QdrantVectorStore(client=qdrant, collection_name="logicspice_products", embedding=embedding)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

question = "What is Logicspice Fiverr Clone?"
docs = retriever.get_relevant_documents(question)

context = "\n\n".join([doc.page_content for doc in docs])
print("🔍 Context:\n", context)

prompt = f"""
You are a helpful and knowledgeable AI chatbot that answers questions specifically about Logicspice products.

Use the context below to provide accurate and concise answers.
If the answer is not in the context, respond with "I don't know."

Context:
{context}

Question: {question}

Answer:
"""

response = llm.invoke(prompt)
print("🤖 Answer:\n", response)
