from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "My salary is 23 LPA",
    "I work at Cotiviti",
    "I am learning Python"
]

q1 = model.encode(["What is my Salary?"])
q2 = model.encode(["What is my CTC?"])
q3 = model.encode(["I love Cricket"])

sim_1_2 = cosine_similarity(q1, q2)[0][0]
sim_1_3 = cosine_similarity(q1, q3)[0][0]


# embeddings = model.encode(sentences)

print(f"Similarity: 'Salary' vs 'CTC': {sim_1_2:.2f}")
print(f"Similarity: 'Salary' vs 'Cricket': {sim_1_3:.2f}")

# print(f"Number of sentences: {len(embeddings)}")
# print(f"Each sentence is now {len(embeddings[0])} numbers")
# print(f"First Embedding (first 5 numbers): {embeddings[0][:5]}")