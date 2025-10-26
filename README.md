# RetrivAI – Document Question Answering Using RAG

Author: Prabhleen Dhesi  
Roll No: 12201153  
Project Type: Hackathon Submission (CloudCosmos – Clone & Elevate)

---

## Introduction

RetrivAI is an AI-based document assistant that allows users to upload documents and ask questions about their content. The system uses Retrieval-Augmented Generation (RAG) to search the uploaded documents and generate accurate answers based on the text found inside them.

This removes the need to manually search long PDFs, notes, or research papers.

---

## How It Works

1. The user uploads one or more documents.
2. The documents are processed and split into small text chunks.
3. These chunks are converted into embeddings and stored in a vector database (ChromaDB).
4. When a question is asked, the system retrieves the most relevant text pieces.
5. The language model (LLM) uses this retrieved information to generate a context-based answer.

---

## Technologies Used

| Part | Technology |
|------|------------|
| Backend | FastAPI |
| Language Model API | Groq API / Hugging Face |
| Embedding Model | Hugging Face Embeddings |
| Vector Storage | ChromaDB |
| Text Processing | LangChain Components |
| Language | Python 3.10+ |

---

## Project Structure

root/
├── app/
│ ├── core/
│ │ ├── document_processor.py
│ │ ├── vector_store.py
│ │ └── llm.py
│ └── routes/
│ ├── documents.py
│ └── chat.py
├── main.py
├── requirements.txt
└── README.md

