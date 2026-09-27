from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b"
)

messages = [
    SystemMessage(content="You are a career coach for developers."),
    HumanMessage(content="I am a React Developer. What should I learn for AI?")
]

response = llm.invoke(messages)
print(response.content)