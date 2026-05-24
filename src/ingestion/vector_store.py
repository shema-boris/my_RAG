# This is where ChromaDB is located. It will consist of sotring and retrieving 

import chromadb
from src.ingestion.embedder import embed_chunks
from langchain.schema import Document


client = chromadb.Client()

def create_collection(collection_name: str):
    collection=client.create_collection(name=collection_name)
    return collection

def get_collection(collection_name:str):
    if collection_name not in client.list_collections():
        raise ValueError(f"Collection {collection_name} does not exist.")
    return client.get_collection(collection_name)

def save_to_vectorstore(chunks:list[Document], collection_name: str):
    collection=get_collection(collection_name)
    ids=[f"chunk_{i}" for i in range(len(chunks))]
    embeddings=embed_chunks(chunks)
    documents=[chunk.page_content for chunk in chunks]
    collection.add(ids=ids, embeddings=embeddings, documents=documents)


