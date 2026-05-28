from sentence_transformers import SentenceTransformer
from langchain.schema import Document

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks: list[Document | str]) -> list[list[float]]:
    texts = [c.page_content if isinstance(c, Document) else c for c in chunks]
    embeddings = model.encode(texts)
    return embeddings.tolist()
