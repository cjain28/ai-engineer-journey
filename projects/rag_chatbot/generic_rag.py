import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def load_document(filepath):
    with open(filepath, "r") as f:
        return f.read()

def chunk_document(document):
    return [chunk.strip() for chunk in document.split(".") if chunk.strip()]

def retrieve_chunks(chunks, question):
    stop_words = ["what", "where", "who", "how", "I", "he", "she" "him", "her", "was",
                  "were", "are", "is", "do", "does"]
    
    keywords = [word.lower() for word in question.split()
                if word.lower() not in stop_words]

    relevant = [chunk for chunk in chunks if any(
        keyword in chunk.lower() for keyword in keywords
    )]

    return relevant if relevant else chunks[:3]

def generate_response(relevant_chunks, question, filename):
    context = "\n".join(relevant_chunks)

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen/qwen3.6-27b",
            "messages": [
                {"role": "system", "content": f"You are a helpful assistant answering questions about {filename}. Answer only using this context:\n{context}"},
                {"role": "user", "content": question}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

print("Generic RAG CHATBOT")
print("-" * 40)

filepath = input("Enter path to your .txt file: ")
filename = os.path.basename(filepath)

document = load_document(filepath)
chunks = chunk_document(document)

print(f"Loaded: {filename}")
print(f"Chunks Created: {len(chunks)}")
print("-" * 40)
print("Ask Anything! Type 'quit' to exit.\n")

while(True):
    question = input("You: ")

    if question.lower() == 'quit':
        print("GoodBye!")
        break

    try:
        relevant = retrieve_chunks(chunks, question)
        answer = generate_response(relevant, question, filename)
        print(f"\n {answer} \n")

    except Exception as e:
        print(f"Error: {e}")
