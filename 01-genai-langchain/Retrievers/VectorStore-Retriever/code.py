from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Create sample documents
documents = [
    Document(
        page_content="Virat Kohli is one of the greatest batsmen in cricket history.",
        metadata={"source": "doc1"},
    ),
    Document(
        page_content="Lionel Messi is an Argentine football player who won the FIFA World Cup in 2022.",
        metadata={"source": "doc2"},
    ),
    Document(
        page_content="Python is a popular programming language used for AI and Machine Learning.",
        metadata={"source": "doc3"},
    ),
    Document(
        page_content="LangChain is a framework for building LLM-powered applications.",
        metadata={"source": "doc4"},
    ),
    Document(
        page_content="ChromaDB is an open-source vector database used to store embeddings.",
        metadata={"source": "doc5"},
    ),
]

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create Chroma Vector Store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Create Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Query
query = "Which database is used for storing embeddings?"

results = retriever.invoke(query)

# Print retrieved documents
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}")
    print("Content :", doc.page_content)
    print("Metadata:", doc.metadata)