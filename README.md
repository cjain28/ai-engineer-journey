# 🚀 AI Engineer Journey

A documented journey from Frontend Developer to AI Engineer: learning Python from scratch, then building LLM chatbots, RAG pipelines and AI agents, one commit at a time.

## 👨‍💻 About
- **Name:** Chirag Jain
- **Current Role:** Frontend Developer (React)
- **Target Role:** AI Engineer
- **Focus:** LLM APIs, RAG systems, embeddings, AI agents

## 🛠️ Projects

### 1. [AI Career Coach](projects/ai-coach)
A career coach for developers moving into AI, built three ways as I learned new tools.
- **CLI chatbot:** multi-turn conversation with memory, using the Groq API directly
- **LangChain intro:** the same idea rebuilt with `ChatGroq` and message objects
- **AI agent:** a LangChain agent that decides when to call custom tools (hike calculator, skills-gap finder)
- **Tech:** Python, Groq API, LLaMA 3.3 70B, GPT-OSS 120B, LangChain

### 2. [RAG Chatbot](projects/rag_chatbot)
Retrieval-Augmented Generation built from scratch, from keyword matching up to vector search.
- **Document Q&A:** load, chunk, retrieve and generate over a text file
- **Generic RAG:** point it at any `.txt` file and chat with it
- **Smart Notes:** type notes, then ask questions about them with conversation memory
- **Semantic RAG:** sentence embeddings and cosine similarity instead of keywords
- **Tech:** Python, Groq API, sentence-transformers, scikit-learn

### 3. [Learnings](projects/learnings)
Day-by-day Python practice: basics, control flow, functions, dictionaries, error handling, OOP and first API calls.

## 📁 Project Structure
```
ai-engineer-journey/
├── projects/
│   ├── ai-coach/        # Chatbot → LangChain → AI agent
│   ├── rag_chatbot/     # Keyword RAG → generic RAG → semantic RAG
│   └── learnings/       # Daily Python exercises
└── README.md
```

## 📚 Learning Path
1. Python fundamentals (variables, loops, functions, list comprehensions)
2. Dictionaries, error handling, OOP, first LLM API calls
3. AI Career Coach: multi-turn chatbot with the Groq API
4. RAG from scratch: chunk, retrieve, generate
5. Generic RAG and Smart Notes assistant
6. Embeddings and semantic search with sentence-transformers
7. LangChain and my first AI agent with tool calling

## ⚙️ Setup
```bash
git clone https://github.com/cjain28/ai-engineer-journey.git
cd ai-engineer-journey
pip install requests python-dotenv langchain langchain-groq sentence-transformers scikit-learn
```

## 🎯 Goal
Become a production-ready AI Engineer by building real projects and documenting everything I learn along the way.
