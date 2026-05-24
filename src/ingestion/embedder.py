from sentence_transformers import SentenceTransformer
from langchain.schema import Document

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks: list[Document]) -> list[list[float]]:
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings.tolist()
