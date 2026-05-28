from src.ingestion.embedder import embed_chunks
from src.ingestion.vector_store import get_collection

def retrieve(query: str, collection_name: str, n_results: int = 5) -> dict:
    query_embedding = embed_chunks([query])
    collection = get_collection(collection_name)
    results = collection.query(query_embeddings=query_embedding, n_results=n_results)
    return results
