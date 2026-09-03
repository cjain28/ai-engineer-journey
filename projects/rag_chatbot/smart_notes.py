import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def get_notes_from_user():
    print("Enter Your Notes Here and Type Done to Finish\n")
    all_notes = []
    while(True):
        note = (input("You: "))
        if note.lower() == 'done':
            print("NOTES ARE SAVED!\n")
            break
        all_notes.append(note)
    return ".".join(all_notes)

def chunk_notes(notes):
    return [chunk.strip() for chunk in notes.split('.') if chunk.strip()]

def retrieve(chunks, question):
    stop_words = ["what", "where", "who", "how", "when", "he", "him", "she", "her", "?", "!", "I", "am", "is", "are"]

    keywords = [word.lower() for word in question.split()
                if word.lower() not in stop_words]

    relevant = [chunk for chunk in chunks if any (
        keyword in chunk.lower() for keyword in keywords
        )]

    return relevant if relevant else chunks

def ask_llm(context, question):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen/qwen3.6-27b",
            "messages": [
                {"role": "system", "content": f"You are a smart notes helper. Answer only usinh this context:\n{context}"},
                {"role": "user", "content": question}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]

def main():
    notes = get_notes_from_user()
    chunks = chunk_notes(notes)
    print(f"{len(chunks)} chunk created\n")

    while True:
        question = input("Ask: ")
        if question.lower() == "quit":
            break
        relevant = retrieve(chunks, question)
        context = "\n".join(relevant)
        answer = ask_llm(context, question)
        print(f"\n {answer} \n")

main()