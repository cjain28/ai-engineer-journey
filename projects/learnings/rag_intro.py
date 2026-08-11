import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

document = """
Chirag Jain is a Frontend Developer with 2 years experience.
He knows React, JavaScript, and CSS.
His current CTC is 23 LPA.
His target is to become an AI Engineer by October 2026.
He is learning Python, LLM APIs, and RAG systems.
"""

chunks = [chunk.strip() for chunk in document.split(".") if chunk.strip()]

print("CHUNKS:")
for i, chunk in enumerate(chunks):
    print(f"{i}: {chunk}")

stop_words = ["what", "is", "a", "an", "the", "of", "chirag's", "whats", "?"]
question = "Whats is Chirag's Ctc ?"

keywords = [word.lower() for word in question.split()
           if word.lower() not in stop_words]

print (f"Keywords: {keywords}")
relevant_chunks= [chunk for chunk in chunks if any(
    keyword in chunk.lower()
    for keyword in keywords
)]

print(f"\nQuestion: {question}")
print(f"Relevant Chunk Found: {relevant_chunks}")

context = "\n".join(relevant_chunks)

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": f"You are answering questions about Chirag Jain. Use only thisclear context:\n{context}"},
            {"role": "user", "content": question}
        ]
    }
)

answer = response.json()["choices"][0]["message"]["content"]
print(f"\nAI Answer: {answer}")