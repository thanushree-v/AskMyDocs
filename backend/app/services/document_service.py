from app.services.pdf_service import extract_text
from app.rag.chunker import chunk_text
from app.services.embedding_service import generate_embedding
from app.rag.vector_service import create_index

def process_document(file):

    text = extract_text(file)

    chunks = chunk_text(text)

    embeddings = [
        generate_embedding(chunk) 
        for chunk in chunks
    ]

    index = create_index(embeddings)

    return {
        "index": index,
        "chunks": chunks,
        "embeddings": embeddings,
        "metadata": {
            "total_characters": len(text),
            "total_chunks": len(chunks),
            "total_embeddings": len(embeddings)
        }
    }

