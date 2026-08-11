import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

body = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": "What is RAG in AI? Explain in 2 lines"}
    ]
}

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=body
)

data = response.json()
# print(data)
print(data["choices"][0]["message"]["content"])