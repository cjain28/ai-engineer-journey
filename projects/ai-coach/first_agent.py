from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b"
)

@tool
def calculate_hike(current_ctc: float, target_ctc: float) -> str:
    """Calculate the hike percentage needed to reach the target CTC"""
    hike = ((target_ctc - current_ctc) / current_ctc) * 100
    return f"You need a {hike:.1f}% hike to go from {current_ctc} LPA to {target_ctc}"

@tool
def get_skills_gap(current_role: str, target_role: str) -> str:
    """Get the skills gap between current and target role"""
    return "Learn Python, ML Fundamentals, LLM APIs, RAG systems"

tools = [calculate_hike, get_skills_gap]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful career Coach. Use Tools when needed.",
    debug=True
)

result = agent.invoke({
    "messages":[{
        "role": "user",
        "content": "I am a frontend developer with 23 LPA CTC. I want to be an AI Engineer with 30 LPA. What hike do I need and what skills should I learn?"
    }]
})

print("\n Final Answer:", result["messages"][-1].content)