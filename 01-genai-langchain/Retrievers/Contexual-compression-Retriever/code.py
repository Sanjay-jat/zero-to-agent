from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

documents = [
    Document(
        page_content="""
Virat Kohli is one of the greatest batsmen in cricket history.
He has scored more than 27000 international runs.
He has captained India across all formats.
He won the ICC Champions Trophy.
He is known for his aggressive batting style and fitness.
"""
    ),
    Document(
        page_content="""
Python is a high-level programming language.
It is widely used in Artificial Intelligence,
Machine Learning, Data Science, Web Development,
Automation, and Backend Development.
"""
    ),
    Document(
        page_content="""
ChromaDB is an open-source vector database.
It stores embeddings generated from text.
It is commonly used in Retrieval-Augmented Generation (RAG)
applications together with LangChain.
"""
    ),
    Document(
        page_content="""
Lionel Messi is an Argentine football player.
He won the FIFA World Cup in 2022.
He has won multiple Ballon d'Or awards.
"""
    ),
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)

base_retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)



llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever,
)



query = "What is ChromaDB used for?"

results = compression_retriever.invoke(query)


for i, doc in enumerate(results, 1):
    print(f"\nResult {i}")
    print("-" * 50)
    print(doc.page_content)