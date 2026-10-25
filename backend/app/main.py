from fastapi import status
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router
from app.api.ask import router as ask_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(ask_router)