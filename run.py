import os
from dotenv import load_dotenv

from lib.aimodel import AIModel

try:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise Exception("OpenAI API key is required")

    ai = AIModel(os.getenv("OPENAI_API_KEY"))

    prompt = ai.prompt_render({
        "variables": {
            "article": "What is data engineering?",
            "format": "json"
        },
        "template": "article_outline"
    })

    print(ai.complete(prompt))
except Exception as e:
    print(e)
