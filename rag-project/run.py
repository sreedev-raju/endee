from rag_pipeline import process_urls, get_rag_answer


urls = [
    "https://devfolio-shine-84.lovable.app/"
]

print("Processing URLs...")
process_urls(urls)

print("\nReady! Ask questions (type 'exit' to quit)\n")

while True:
    query = input("Enter your question: ")

    if query.lower() == "exit":
        break

    answer = get_rag_answer(query)

    print("\nAnswer for Sreedev:\n", answer)
    print("-" * 50)