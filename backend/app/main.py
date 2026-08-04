from fastapi import status
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "Welcome to AskMyDocs API"
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

@app.post("/upload")
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
    

    
    return {
        "message": "PDF uploaded successfully.",
        "filename" : file.filename,
        "content_type" : file.content_type
    }