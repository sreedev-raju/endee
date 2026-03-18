# 🧠 Endee RAG AI Assistant

## 📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) based AI assistant that extracts and answers questions from portfolio/webpage content.

---

## 🚀 Features

* Extract data from portfolio URLs
* Store embeddings in a vector store
* Retrieve relevant content using similarity search
* Answer user queries based on retrieved context

---

## 🏗️ System Design

1. Data Ingestion (scraper.py)
2. Embedding + Storage (vector_store.py)
3. Retrieval (rag_pipeline.py)
4. UI (app.py)

---

## ⚙️ Tech Stack

* Python
* Sentence Transformers
* BeautifulSoup
* Streamlit

---

##  Use of Endee

This project is built on top of the Endee repository as required and follows its structure while implementing a RAG pipeline.

---

##  How to Run

```bash
git clone https://github.com/sreedev-raju/endee.git
cd endee/rag-project
pip install -r requirements.txt
python run.py
```

---

##  Example Query

What are Sreedev's skills?

---

##  Author

Sreedev
