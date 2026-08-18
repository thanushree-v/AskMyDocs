import math

from app.services.embedding_service import generate_embedding


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    return dot_product / (magnitude_a * magnitude_b)


text_a = "TCP provides reliable delivery."
text_b = "TCP ensures data is delivered reliably."
text_c = "Chocolate cake requires flour and sugar."


embedding_a = generate_embedding(text_a)
embedding_b = generate_embedding(text_b)
embedding_c = generate_embedding(text_c)


print("A ↔ B:", cosine_similarity(embedding_a, embedding_b))
print("A ↔ C:", cosine_similarity(embedding_a, embedding_c))
print("B ↔ C:", cosine_similarity(embedding_b, embedding_c))