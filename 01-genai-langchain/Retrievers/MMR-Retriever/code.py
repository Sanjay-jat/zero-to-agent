from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="Virat Kohli is an Indian cricketer."),
    Document(page_content="Python is a programming language."),
    Document(page_content="ChromaDB is a vector database."),
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "fetch_k": 3
    }
)

results = retriever.invoke("Tell me about vector databases")

for doc in results:
    print(doc.page_content)