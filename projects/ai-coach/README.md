# 🤖 AI Career Coach

A career coach for developers moving into AI Engineering, built three times as I learned new tools: raw API calls, then LangChain, then a tool-using AI agent.

## 📂 Files
| File | What it does |
|------|--------------|
| `ai_coach.py` | Multi-turn CLI chatbot that calls the Groq API directly and keeps conversation history |
| `langchain_intro.py` | The same coach rebuilt with LangChain's `ChatGroq`, `SystemMessage` and `HumanMessage` |
| `first_agent.py` | A LangChain agent that decides on its own when to call custom tools |

## 🔧 How it works

### CLI chatbot (`ai_coach.py`)
1. Starts the conversation with a system prompt ("career coach for a UI developer")
2. Reads your message from the terminal
3. Appends it to the conversation history and sends the full history to LLaMA 3.3 70B via Groq
4. Prints the reply and saves it to history, so the coach remembers earlier messages
5. Type `quit` to exit

### AI agent (`first_agent.py`)
The agent has two tools defined with LangChain's `@tool` decorator:
- **`calculate_hike`**: works out the percentage hike between current and target CTC
- **`get_skills_gap`**: returns the skills needed to move from one role to another

Given one question, the agent decides which tools to call, runs them, and combines the results into a final answer. `debug=True` prints each reasoning and tool-call step.

## 🛠️ Tech Stack
- Python
- Groq API
- LLaMA 3.3 70B, GPT-OSS 120B
- LangChain (`langchain`, `langchain-groq`, `langchain-core`)
- python-dotenv

## ▶️ How to run
1. Install dependencies: `pip install requests python-dotenv langchain langchain-groq`
2. Add your `GROQ_API_KEY` to `.env`
3. Run one of:
   ```bash
   python ai_coach.py         # interactive chatbot
   python langchain_intro.py  # single LangChain call
   python first_agent.py      # tool-calling agent
   ```

## 📸 Example
```
YOU: I am a React developer, what should I learn for AI?

 Coach: As a React developer, focus on:

1. **Python**: Learn Python basics, essential for most AI frameworks.
2. **TensorFlow or PyTorch**: Choose one and learn the fundamentals of AI development.
3. **Machine Learning**: Study supervised, unsupervised, and reinforcement learning.
4. **Deep Learning**: Focus on neural networks, CNNs and RNNs.
5. **Data Preprocessing**: Learn to work with datasets, data visualization, and feature engineering.

Start with Python and TensorFlow/PyTorch tutorials, then move to more advanced AI topics.
```

## 💡 What I learned
- How chat APIs use `system`, `user` and `assistant` roles, and why you resend the whole history
- How LangChain wraps LLM providers behind one interface
- How agents pick tools based on their docstrings and type hints
