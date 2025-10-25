from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.vector_store import find_related_documents
from app.core.llm import generate_answer

router = APIRouter()

class ChatQuery(BaseModel):
    query: str

@router.post("/chat/")
async def chat_with_documents(chat_query: ChatQuery):
    """
    Receives a user query, finds relevant documents, and generates a response.
    """
    try:
        relevant_docs = find_related_documents(chat_query.query)
        if not relevant_docs:
            return {"answer": "I could not find any relevant information in the uploaded documents to answer your question."}
            
        ai_response = generate_answer(chat_query.query, relevant_docs)
        return {"answer": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))