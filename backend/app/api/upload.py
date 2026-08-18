from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.document_service import process_document
from app.services.document_store import documents
router = APIRouter(
    prefix="/api",
    tags=["Upload"]
)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid File Type"
        )

    header = file.file.read(5)

    if header != b"%PDF-":
        raise HTTPException(
            status_code = 400,
            detail = "Not a PDF file"
        )

    file.file.seek(0)

    document = process_document(file.file)

    documents["current"] = document
  
    return {
    "message": "PDF indexed successfully.",
    "filename": file.filename,
    "content_type": file.content_type,
    "metadata": document["metadata"]
    }