def generate_prompt(query: str, context: str) -> str:
    prompt = f"""You are a helpful assistant. Answer the user's question using only the context provided below.
If the answer is not in the context, say "I don't have enough information to answer that."

Context:
{context}

Question:
{query}

Answer:"""
    return prompt