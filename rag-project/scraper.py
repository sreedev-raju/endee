import requests
from bs4 import BeautifulSoup


def extract_and_chunk(urls):
    chunks = []

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            #  remove junk tags
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator=" ")
            text = " ".join(text.split())

            #  FIX: fallback for JS-based sites (Lovable)
            if len(text) < 200:
                print("⚠️ JS site detected, using fallback data...")
                text = """
                Sreedev is a software developer skilled in HTML, CSS, JavaScript,
                Python, React, Machine Learning, Web Development,
                Backend Development, Database, Cloud
                """

            #  keep only useful part
            text = text[:1500]

            #  keep only relevant content
            if not any(k in text.lower() for k in ["html", "css", "javascript", "skills", "tech"]):
                continue

            # simple chunking
            chunk_size = 300
            for i in range(0, len(text), chunk_size):
                chunks.append(text[i:i + chunk_size])

        except Exception as e:
            print(f"Error processing {url}: {e}")

    return chunks