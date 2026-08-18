from app.services.embedding_service import generate_embedding

text = "TCP provides reliable delivery."

embedding = generate_embedding(text)

print("Vector type:", type(embedding))
print("Vector dimensions:", len(embedding))
print("First 10 values:", embedding[:10])