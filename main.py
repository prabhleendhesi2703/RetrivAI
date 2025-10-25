from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes import documents, chat

# Load environment variables from .env file
load_dotenv()

# Check for Google API Key
if not os.getenv("GOOGLE_API_KEY"):
    raise Exception("GOOGLE_API_KEY environment variable not found.")

app = FastAPI(
    title="DocuMind AI - RAG Backend",
    description="RetrivAI backend API.",
    version="1.0.0"
)

# Include the API routers
app.include_router(documents.router, prefix="/api/v1", tags=["Documents"])
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the DocuMind AI RAG Backend. Visit /docs for the API documentation."}