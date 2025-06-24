from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.langchain.rag_chain import get_rag_chain
from uuid import uuid4
from app.db.mongo_logger import log_chat
import traceback

router = APIRouter()


class ChatRequest(BaseModel):
    user_id: str
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        # Create or fetch RAG chain for this user
        rag_chain = get_rag_chain(request.user_id)

        # Invoke chain
        result = rag_chain.invoke({"question": request.question})

        answer = result["answer"]

        # Optional: derive user_name from user_id or send from frontend
        user_name = request.user_id  

        # Save to MongoDB
        log_chat(
            user_id=request.user_id,
            user_name=user_name,
            question=request.question,
            answer=answer
        )


        return {
            "question": request.question,
            "answer": result["answer"],
            "sources": [
                {
                    "id": doc.metadata.get("_id") or doc.metadata.get("id"),
                    "title": doc.metadata.get("title") or None,
                    "description": doc.metadata.get("page_content") or doc.page_content[:200]
                }
                for doc in result.get("source_documents", [])
            ]
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
