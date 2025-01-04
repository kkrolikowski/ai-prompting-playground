import os
from dotenv import load_dotenv

from lib.aimodel import AIModel

load_dotenv()

ai = AIModel(os.getenv("OPENAI_API_KEY"))

prompt = ai.prompt_render({
  "variables": {"article": "What is data engineering?", "format": "yaml"},
  "template": "article_outline"
})

print(ai.complete(prompt))