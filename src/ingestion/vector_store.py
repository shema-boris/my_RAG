import chromadb
from langchain.schema import Document
from src.ingestion.embedder import embed_chunks

client = chromadb.PersistentClient(path="data/chroma")

def get_collection(collection_name: str):
    existing = [c.name for c in client.list_collections()]
    if collection_name not in existing:
        raise ValueError(f"Collection '{collection_name}' does not exist.")
    return client.get_collection(collection_name)

def save_to_vectorstore(chunks: list[Document], collection_name: str) -> None:
    collection = client.get_or_create_collection(name=collection_name)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    embeddings = embed_chunks(chunks)
    documents = [chunk.page_content for chunk in chunks]
    collection.add(ids=ids, embeddings=embeddings, documents=documents)
    print(f"Saved {len(chunks)} chunks to collection '{collection_name}'")
    


