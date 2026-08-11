import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}", 
    # Bearer is the authentication most AI Api use
    "Content-Type": "application/json"
}

conversation = [
    {"role": "system", "content": "You are a career coach helping a UI developer transition to AI engineering. Keep answers concise and practical."}
]

print("AI Coach - Type 'quit' to exit\n")

while True:
    user_input = input("YOU: ")

    if user_input.lower() == "quit":
        print(" All the best! ")
        break

    conversation.append({"role": "user", "content": user_input})

    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": conversation
    }

    try :
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=body
        )
        data = response.json()
        reply = data["choices"][0]["message"]["content"]

        conversation.append({"role": "assistant", "content": reply})

        print(f"\n Coach: {reply}\n")

    except Exception as e:
        print(f"Error: {e}")