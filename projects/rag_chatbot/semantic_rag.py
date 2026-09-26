from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_notes_from_user():
    print("Enter your notes (type done to finish)\n")
    all_notes = []
    while True:
        note = input("You: ")
        if note.lower() == 'done':
            break
        sentences = [s.strip() for s in note.split('.') if s.strip()]
        all_notes.extend(sentences)
    return all_notes

def find_relevant_chunks(chunks, question, top_k=2):
    embedding_chunks = model.encode(chunks)
    embedding_question = model.encode([question])

    similarities = cosine_similarity(embedding_question, embedding_chunks)[0]
    
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]

def ask_llm(context, question):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-120b",
            "messages": [
                {"role": "system", "content": f"Answer using only this context:\n{context}"},
                {"role": "user", "content": question}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

def main():
    chunks = get_notes_from_user()
    print(f"\n{len(chunks)} notes loaded\n")

    while True:
        question = input("Ask: ")
        if question.lower() == "quit":
            break
        relevant = find_relevant_chunks(chunks, question)
        print(f"Retrieved: {relevant}")
        context = "\n".join(relevant)
        answer = ask_llm(context, question)
        print(f"\n {answer} \n")

main()