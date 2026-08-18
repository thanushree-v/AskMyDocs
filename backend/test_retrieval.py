from app.services.embedding_service import generate_embedding
from app.rag.vector_service import create_index
from app.rag.vector_service import retrieve_chunks


texts = [
    "TCP provides reliable delivery.",
    "TCP ensures data is delivered reliably.",
    "Chocolate cake requires flour and sugar."
]

embeddings = [
    generate_embedding(text)
    for text in texts
]

index = create_index(embeddings)

results = retrieve_chunks(
    index,
    texts,
    "Which protocol provides reliable delivery?",
    top_k=2
)

for result in results:
    print("\nScore:", result["score"])
    print("Text:", result["text"])