from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def chunk_text(text: str) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.create_documents([text])