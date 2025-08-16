import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast and effective

def load_documents():
    with open("chatbot/knowledge/documents.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = []
    sources = []
    for doc in data:
        content = doc.get("answer") or doc.get("content") or ""
        source = doc.get("question") or doc.get("title") or "unknown"
        texts.append(content)
        sources.append(source)
    return texts, sources

def chunk_texts(texts, chunk_size=500):
    chunks = []
    for text in texts:
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i+chunk_size])
    return chunks

def get_answer_from_docs(user_question):
    texts, sources = load_documents()
    chunks = chunk_texts(texts)

    # Encode chunks and question
    chunk_embeddings = model.encode(chunks)
    question_embedding = model.encode([user_question])

    # Find best match
    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]
    top_idx = int(np.argmax(similarities))

    return chunks[top_idx]

# Direct testing
if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        ans = get_answer_from_docs(q)
        print("Answer:", ans)
