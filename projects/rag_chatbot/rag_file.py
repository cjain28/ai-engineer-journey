import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Step1: Load the text from .txt file
with open("chirag_profile.txt", "r") as f:
    document = f.read()

print("Document Loaded Successfully")
print(f"Total Characters {len(document)}")

# Step2: chunk

chunks = [chunk.strip() for chunk in document.split(".") if chunk.strip()]

print(f"Total Chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"{i}: {chunk}")

# Step3: Retrieve

stop_words = ["What", "is", "a", "the", "an", "of", "his", "he", "him", "?", "Whats", "where", "does"]
question = input(f"\nAsk anything about Chirag: ")

keywords = [word.lower() for word in question.split()
           if word.lower() not in stop_words]

print(f"keywords: {keywords}")

relevant_chunks = [chunk for chunk in chunks if any(
    keyword in chunk.lower() for keyword in keywords
)]

print(f"Relevant-chunks: {relevant_chunks}")

# Step4: Generate

context = "\n" .join(relevant_chunks)

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": f"You are answering about Chirag. Use this Clear context: \n{context}"},
            {"role": "user", "content": question}
        ]
    }
)

answer = response.json()["choices"][0]["message"]["content"]
print(f"\nAnswer: {answer}")