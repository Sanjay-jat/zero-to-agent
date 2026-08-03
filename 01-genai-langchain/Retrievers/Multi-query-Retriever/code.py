from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_classic.retrievers import MultiQueryRetriever
from dotenv import load_dotenv
load_dotenv()


documents = [
    Document(page_content="Virat Kohli is one of the greatest batsmen in cricket history."),
    Document(page_content="MS Dhoni is one of the most successful captains of India."),
    Document(page_content="Lionel Messi won the FIFA World Cup in 2022."),
    Document(page_content="Python is widely used for Artificial Intelligence and Machine Learning."),
    Document(page_content="ChromaDB is a vector database used in Retrieval-Augmented Generation (RAG)."),
]


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# Multi Query Retriever
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)


query = "Tell me about vector databases."


results = multi_query_retriever.invoke(query)


for i, doc in enumerate(results, 1):
    print(f"\nResult {i}")
    print(doc.page_content)