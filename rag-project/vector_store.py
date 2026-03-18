import endee

# simple in-memory storage (Endee wrapper style)
db = []


def store_embeddings(texts, embeddings):
    global db
    db = []

    for text, emb in zip(texts, embeddings):
        db.append({
            "embedding": emb,
            "metadata": {"text": text}
        })


def similarity(a, b):
    return sum(x * y for x, y in zip(a, b))


def search_embeddings(query_embedding, top_k=2):
    scored = []

    for item in db:
        score = similarity(query_embedding, item["embedding"])
        scored.append((score, item))

    scored.sort(reverse=True)

    return [item for _, item in scored[:top_k]]