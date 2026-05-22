# Loader.py will write functions about loading documents for the data folder

import pypdf
def load_document(file_path: str) -> str:
    # Checks the file extension (.pdf, .md, .txt)
    #Use pypdf to extract text from documents
    # Use plain open() for markdown/text files
    #return a single raw string
    
    if file_path.endswith('.pdf'):
        reader = pypdf.PdfReader(file_path)
        text=""
        for page in reader.pages:
            text+=page.extract_text()
        return text
    
    elif file_path.endswith('.md') or file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type: Please provide a pdf, markdown or text file")