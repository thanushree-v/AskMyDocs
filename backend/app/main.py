from fastapi import status
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.api.upload import router as upload_router
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

app.include_router(upload_router)