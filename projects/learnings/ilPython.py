def retrieve(sentences, question):

    chunks = [chunk.strip() for chunk in sentences]

    stop_words = ["what", "is", "the", "?"]

    keywords = [word.strip("?") for word in question.split() if word.lower().strip("?") not in stop_words]

    relevant = []
    for chunk in chunks:
        for keyword in keywords:
            if keyword.lower() in chunk.lower() and chunk not in relevant:
                relevant.append(chunk)

    return relevant

# Test it
sentences = ["I love Python", "React is great", "AI is the future"]
question = "What about Python?"
print(retrieve(sentences, question))