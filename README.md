```markdown
# RetrivAI – Document Question Answering Using RAG

Author: Prabhleen Dhesi  
Roll No: 12201153  
Project Type: Hackathon Submission (CloudCosmos – Clone & Elevate)

---

## Introduction

RetrivAI is an AI-based document assistant that lets users upload documents and ask questions about their content. The system uses Retrieval-Augmented Generation (RAG) to search uploaded documents and generate answers based on the text found inside them.

---

## How It Works

1. User uploads one or more documents.
2. Documents are processed and split into text chunks.
3. Chunks are converted into embeddings and stored in a vector database (ChromaDB).
4. When a question is asked, the system retrieves the most relevant chunks.
5. A language model (LLM) generates an answer using the retrieved context.

---

## Technologies Used

| Part                | Technology                      |
|---------------------|----------------------------------|
| Backend             | FastAPI                          |
| Language Model API  | Groq API / Hugging Face          |
| Embeddings          | Hugging Face Embeddings          |
| Vector Database     | ChromaDB                         |
| Text Processing     | LangChain components             |
| Language            | Python 3.10+                     |

---

## Project Structure



root/
├── app/
│   ├── core/
│   │   ├── document_processor.py
│   │   ├── vector_store.py
│   │   └── llm.py
│   └── routes/
│       ├── documents.py
│       └── chat.py
├── main.py
├── requirements.txt
└── README.md

````

---

## Setup Instructions 



### 1) Clone the repository
```bash
git clone https://github.com/prabhleendhesi2703/RetrivAI/
cd RetrivAI-main
````

### 2) Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux (bash / zsh)**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Create a `.env` file in the project root

Open a new file named `.env` and add the required API keys:

```
GROQ_API_KEY=<your_groq_api_key>
HUGGINGFACEHUB_API_TOKEN=<your_huggingface_token>
```

Replace the placeholders with actual keys.

### 5) Start the development server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6) Open the API docs in your browser

```
http://localhost:8000/docs
```

---

## Usage

### Upload Documents

**Endpoint**

```
POST /api/v1/upload-documents/
```

**Form-data**

* `files`: one or more files (PDF, DOCX, TXT)

**curl example**

```bash
curl -X POST "http://localhost:8000/api/v1/upload-documents/" \
  -F "files=@/path/to/doc1.pdf" \
  -F "files=@/path/to/doc2.docx"
```

### Ask a Question

**Endpoint**

```
POST /api/v1/chat/
```

**JSON body example**

```json
{
  "query": "Summarize the introduction section of the uploaded document."
}
```

**curl example**

```bash
curl -X POST "http://localhost:8000/api/v1/chat/" \
  -H "Content-Type: application/json" \
  -d '{"query":"How do I run the app locally?"}'
```

---

## Demo Video

```
https://youtu.be/<your-demo-id>
```

---

## Limitations

* Requires internet access for Groq and Hugging Face API calls.
* Large documents increase processing time.
* Answer quality depends on embedding model, chunk size, and chosen LLM.

---

## Developed by

Prabhleen Dhesi
Roll No: 12201153
