import faiss
import numpy as np
from app.services.embedding_service import generate_embedding
from app.services.vector_service import create_index


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

print("Number of vectors:", index.ntotal)
print("Vector dimensions:", index.d)

query = "Which protocol provides reliable delivery?"

query_embedding = generate_embedding(query)

query_vector = np.array([query_embedding]).astype("float32")

faiss.normalize_L2(query_vector)

distances, indices = index.search(query_vector, k=2)

print("Indices:", indices)
print("Scores:", distances)