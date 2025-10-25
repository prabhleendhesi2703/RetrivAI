from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes import documents, chat

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise Exception("GROQ_API_KEY environment variable not found.")

app = FastAPI(
    title="RetrivAI - RAG Backend",
    description="RetrivAI backend API.",
    version="1.0.0"
)

app.include_router(documents.router, prefix="/api/v1", tags=["Documents"])
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the RetrivAI RAG Backend. Visit /docs for the API documentation."}