import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from scraper import extract_and_chunk
from vector_store import store_embeddings, search_embeddings


def simple_embedding(text):
    return [len(text), sum(ord(c) for c in text) % 1000]



def process_urls(urls):
    chunks = extract_and_chunk(urls)

    embeddings = [simple_embedding(chunk) for chunk in chunks]

    store_embeddings(chunks, embeddings)

    return "Data processed and stored in Endee!"



def extract_skills(text):
    text = text.lower()

    skill_map = {
       
        "html": "HTML",
        "css": "CSS",
        "javascript": "JAVASCRIPT",
        "bootstrap": "BOOTSTRAP",
        "react": "REACT",

        
        "python": "PYTHON",
        "java": "JAVA",

       
        "machine learning": "MACHINE LEARNING",
        "data science": "DATA SCIENCE",
        "web development": "WEB DEVELOPMENT",
        "backend development": "BACKEND DEVELOPMENT",
        "computer vision": "COMPUTER VISION",
        "algorithms": "ALGORITHMS",
        "database": "DATABASES",
        "cloud": "CLOUD"
    }

    found = []

    for key, value in skill_map.items():
        if key in text:   
            found.append(value)

   
    found = list(set(found))

    return ", ".join(found) if found else "No skills found"



def get_rag_answer(query):
    query_embedding = simple_embedding(query)

    results = search_embeddings(query_embedding, top_k=3)

    if not results:
        return "No relevant data found."

    context = "\n".join([
        r["metadata"]["text"]
        for r in results
    ])

    print("\nRetrieved Context:\n", context)  
    if not context.strip():
        return "No skills found"

    clean_answer = extract_skills(context)

    return clean_answer