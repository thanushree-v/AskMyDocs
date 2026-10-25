from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.document_store import documents
from app.rag.vector_service import retrieve_chunks
from app.services.llm_service import generate_answer

router = APIRouter(
    prefix="/api",
    tags=["Ask"]
)

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):

    if "current" not in documents:
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first."
        )

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    document = documents["current"]

    results = retrieve_chunks(
        document["index"],
        document["chunks"],
        request.question,
        top_k=3
    )

    if not results:
        return {
            "question": request.question,
            "answer" : "I couldn't find relevant information in the uploaded document.",
            "sources": []
        }
    
    context = "\n\n".join(
        result["text"]
        for result in results
    )

    try:
        answer = generate_answer(
            request.question,
            context
        )
    except Exception as e:
        print(f"[ERROR] LLM generation failed: {type(e).__name__}: {e}")
        raise HTTPException(
            status_code=502,
            detail="Unable to generate an answer right now."
        )

    return {
        "question": request.question,
        "answer": answer,
        "sources":[
        {
        "source_id": i + 1,
        "score": source["score"],
        "text": source["text"]
        }
        for i, source in enumerate(results)
        ]
    }