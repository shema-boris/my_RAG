from src.generation.generator import generate_response
from src.utils.config import COLLECTIONS

def main():
    print("RAG System ready. Type 'quit' to exit.\n")
    collection_name = COLLECTIONS["general"]

    while True:
        query = input("You: ").strip()
        if not query:
            continue
        if query.lower() == "quit":
            break

        answer = generate_response(query, collection_name=collection_name)
        print(f"\nAssistant: {answer}\n")

if __name__ == "__main__":
    main()
