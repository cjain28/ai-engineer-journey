# 🤖 RAG Chatbot

Retrieval-Augmented Generation (RAG) built from scratch in Python. It starts with simple keyword matching and ends with semantic vector search using sentence embeddings.

## 🎯 What is RAG?
LLMs don't know about your documents. RAG fixes that in three steps:
1. **Chunk:** split the document into small pieces
2. **Retrieve:** find the pieces relevant to the question
3. **Generate:** send only those pieces plus the question to the LLM, so it answers from your data

## 📂 Files
| File | What it does | Retrieval |
|------|--------------|-----------|
| `rag_file.py` | Q&A over `chirag_profile.txt` | Keyword match |
| `generic_rag.py` | Chat with **any** `.txt` file you point it at | Keyword match, falls back to the first 3 chunks |
| `smart_notes.py` | Type notes, then ask questions about them, with conversation memory | Keyword match |
| `embeddings_test.py` | Shows how similar sentences get similar embeddings | Cosine similarity demo |
| `semantic_rag.py` | Notes Q&A using vector search | Embeddings + cosine similarity (top-k) |
| `chirag_profile.txt` | Sample document for `rag_file.py` | n/a |

## 🔧 How it evolved

### 1. Keyword RAG (`rag_file.py`)
1. **Load:** reads a `.txt` file
2. **Chunk:** splits it into sentences
3. **Retrieve:** removes stop words from the question, keeps chunks containing any keyword
4. **Generate:** sends context + question to LLaMA 3.3 70B

### 2. Generic RAG (`generic_rag.py`)
The same pipeline refactored into reusable functions (`load_document`, `chunk_document`, `retrieve_chunks`, `generate_response`), with a chat loop that works on any file.

### 3. Smart Notes (`smart_notes.py`)
Builds the knowledge base from notes you type in, and keeps chat history so follow-up questions work.

### 4. Semantic RAG (`semantic_rag.py`)
Keyword matching misses synonyms ("salary" vs "CTC"). This version:
1. Encodes every note with `all-MiniLM-L6-v2` from sentence-transformers
2. Encodes the question the same way
3. Ranks notes by cosine similarity and takes the top 2
4. Sends them to the LLM as context

## 🛠️ Tech Stack
- Python
- Groq API (LLaMA 3.3 70B, Qwen, GPT-OSS 120B)
- sentence-transformers (`all-MiniLM-L6-v2`)
- scikit-learn (cosine similarity)
- python-dotenv

## ▶️ How to run
1. Install dependencies: `pip install requests python-dotenv sentence-transformers scikit-learn`
2. Add your `GROQ_API_KEY` to `.env`
3. Run from this folder:
   ```bash
   python rag_file.py       # ask about the sample profile
   python generic_rag.py    # enter a path to any .txt file
   python smart_notes.py    # type notes, then "done", then ask questions
   python semantic_rag.py   # same as smart notes, with vector search
   ```
   Type `quit` to exit the chat loops.

## 📸 Example
```
Ask anything about Chirag: Where does Chirag live?
Answer: Chirag lives in Delhi.
```
`embeddings_test.py` prints a much higher similarity for "Salary" vs "CTC" than for "Salary" vs "Cricket", even though "Salary" and "CTC" share no words. That's why semantic search beats keyword search.

## 💡 What I learned
- Why chunk size and retrieval quality matter more than the model
- Where keyword search breaks (synonyms, phrasing) and how embeddings fix it
- How to turn a script into reusable functions
