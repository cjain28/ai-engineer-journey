def chunk_by_newline(text):
    return [chunk.strip() for chunk in text.split('\n') if chunk.strip() ]

text = "I love Python\nReact is great\nAI is the future"
print(chunk_by_newline(text))