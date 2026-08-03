##wikipedia-retriever
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2)

docs = retriever.invoke("Virat Kohli")

for doc in docs:
    print(doc.metadata["title"])
    print(doc.page_content[:500])