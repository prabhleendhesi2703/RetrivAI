import os
import traceback  # <-- IMPORT THIS MODULE AT THE TOP
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from app.core.document_processor import load_document, chunk_documents
from app.core.vector_store import index_documents, clear_vector_store

router = APIRouter()
docstore_path = "./docstore/"
os.makedirs(docstore_path, exist_ok=True)

@router.post("/upload-documents/")
async def upload_documents(files: List[UploadFile] = File(...)):
    """
    Uploads multiple documents, processes them, and indexes them.
    """
    saved_paths = []
    try:
        for file in files:
            file_path = os.path.join(docstore_path, file.filename)
            with open(file_path, "wb") as f:
                f.write(await file.read())
            saved_paths.append(file_path)

        all_chunks = []
        for path in saved_paths:
            raw_documents = load_document(path)
            processed_chunks = chunk_documents(raw_documents)
            all_chunks.extend(processed_chunks)
        
        if all_chunks:
            index_documents(all_chunks)
            
        return {"message": f"Successfully processed and indexed {len(files)} document(s)."}
    except Exception as e:
        # --- ADD THESE TWO LINES TO SEE THE FULL ERROR ---
        print("An error occurred during document processing:")
        traceback.print_exc()
        # --------------------------------------------------

        # Clean up saved files in case of an error
        for path in saved_paths:
            if os.path.exists(path):
                os.remove(path)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/clear-documents/")
async def clear_documents():
    """
    Clears all documents from the vector store.
    """
    try:
        clear_vector_store()
        return {"message": "All documents have been cleared from the vector store."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))