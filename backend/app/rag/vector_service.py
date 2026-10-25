import faiss
import numpy as np


def create_index(embeddings):
    dimension = len(embeddings[0])

    vectors = np.array(embeddings).astype("float32")

    faiss.normalize_L2(vectors)

    index = faiss.IndexFlatIP(dimension)

    index.add(vectors)

    return index

from app.services.embedding_service import generate_embedding
def retrieve_chunks(index, chunks, question, top_k=3, score_threshold=0.60):
    
    query_embedding = generate_embedding(question)

    query_vector = np.array(
        [query_embedding]
    ).astype("float32")

    faiss.normalize_L2(query_vector)

    top_k = min(top_k,len(chunks))

    scores,indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for score, index_position in zip(scores[0],indices[0]):
        
        if score < score_threshold:
            continue
        
        results.append(
            {
                "text": chunks[index_position],
                "score": float(score)
            }
        )
    
    return results
    