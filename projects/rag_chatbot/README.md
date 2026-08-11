# 🤖 RAG Chatbot

A document Q&A system built from scratch using Python and LLaMA 3.3 70B.

## 🎯 What it does
Ask any question about a document and get accurate AI-powered answers.

## 🔧 How it works
1. **Load** — Reads a `.txt` file
2. **Chunk** — Splits document into sentences
3. **Retrieve** — Finds relevant chunks using keyword matching
4. **Generate** — Sends context + question to LLM → gets answer

## 🛠️ Tech Stack
- Python
- Groq API
- LLaMA 3.3 70B
- python-dotenv

## ▶️ How to run
1. Clone the repo
2. Add your `GROQ_API_KEY` in `.env`
3. Run `python rag_file.py`
4. Ask any question about Chirag!

## 📸 Example
```
Ask anything about Chirag: Where does Chirag live?
Answer: Chirag lives in Delhi.
```