from openai import OpenAI
from src.retrieval.retriever import retrieve
from src.generation.prompts import generate_prompt
from src.utils.config import get_config, COLLECTIONS

client = OpenAI(api_key=get_config()["openai_api_key"])

def generate_response(query: str, collection_name: str = COLLECTIONS["general"]) -> str:
    results = retrieve(query, collection_name=collection_name)
    context = "\n\n".join(results["documents"][0])
    prompt = generate_prompt(query, context)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content