import os
from dotenv import load_dotenv

load_dotenv()

COLLECTIONS = {
    "general": "general",
}

def get_config() -> dict:
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
    }
