# 🤖 AI Career Coach

A conversational CLI chatbot that helps developers transition into AI Engineering.

## 🎯 What it does
A CLI-based AI career coach that gives personalized guidance to developers looking to switch into AI engineering roles.

## 🔧 How it works
1. Takes user input from terminal
2. It saves the conversation history.
3. Sends to LLaMA 3.3 70B via Groq API
4. It fetches out a response with career building guide.

## 🛠️ Tech Stack
- Python
- Groq API
- LLaMA 3.3 70B
- python-dotenv

## ▶️ How to run
1. Clone the repo
2. Add your `GROQ_API_KEY` in `.env`
3. Run `python ai_coach.py`
4. Enter your info with a question

## 📸 Example
```
You: I am a React developer, what should I learn for AI?
Coach:  Coach: As a React developer, focus on:

1. **Python**: Learn Python basics, essential for most AI frameworks.
2. **TensorFlow or PyTorch**: Choose one and learn the fundamentals of AI development.
3. **Machine Learning**: Study supervised, unsupervised, and reinforcement learning.
4. **Deep Learning**: Focus on neural networks, convolutional neural networks (CNNs), and recurrent neural networks (RNNs).
5. **Data Preprocessing**: Learn to work with datasets, data visualization, and feature engineering.

Start with Python and TensorFlow/PyTorch tutorials, then move to more advanced AI topics.
```