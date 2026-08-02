# 🗄️ Vector Stores with Chroma
 
Today I finally connected the dots on *where do embeddings actually live?* Turns out — a vector store. Spent the session doing full CRUD (yes, all four operations) on a Chroma vector store using Gemini embeddings, and honestly it clicked way faster than I expected.
 
## 💡 Concept
 
A vector store is a database built specifically to store embeddings and let you search through them by *meaning* instead of exact keywords. You dump `Document` objects in, it converts them to vectors under the hood using an embedding model, and then you can ask it "find me things similar to X" and get back ranked, relevant results — even if the wording doesn't match at all.
 
Chroma is one of the simplest vector stores to get started with — lightweight, works locally with a `persist_directory`, and plugs straight into LangChain.
 
## 🛠️ What I built
 
Set up a small Chroma collection with three `Document` objects (cricketers, because why not) and Gemini's `gemini-embedding-001` model, then ran it through the full lifecycle:
 
- **Created** a `Chroma` vector store with a named collection and persistence
- **Added** documents with metadata (`team: Rcb`, `team: csk`)
- **Viewed** stored documents along with their raw embeddings
- **Searched** using `similarity_search()` and `similarity_search_with_score()`
- **Updated** an existing document's content in place
- **Deleted** a document by its ID and confirmed it was gone
## 🔑 Key Learnings
 
- Every document gets a unique auto-generated ID when added — you'll need to capture these if you plan to update or delete later
- `similarity_search()` returns just the matching `Document` objects, while `similarity_search_with_score()` also gives you a distance/similarity score — useful when you want to filter out weak matches
- Lower score ≠ always "better" — it depends on the distance metric Chroma is using under the hood, so don't assume it's a plain similarity percentage
- `vector_store.get(include=[...])` is the way to peek inside the store — you can pull back `embeddings`, `documents`, or `metadatas` selectively instead of dumping everything
- `update_document()` needs the exact `document_id` — it doesn't match by content, so you have to track IDs from the moment you add documents
- Metadata (like `team`) sticks to the document and can later be used for filtering searches, even though I didn't filter on it yet today
- `persist_directory` means the collection survives across sessions — it's not just an in-memory toy store
## 🧾 Code Snippet
 
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
 
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key="your_actual_api_key_here"
)
 
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="chroma_db",
)
 
doc1 = Document(
    page_content="Virat kohli is an indian cricketer and a batsman",
    metadata={"team": "Rcb"}
)
 
vector_store.add_documents([doc1])
 
# search
vector_store.similarity_search_with_score(
    query="who are the batsmen in indian cricket team?",
    k=2
)
 
# update
update_doc1 = Document(
    page_content="Virat kohli is an indian cricketer, a batsman, and former RCB captain",
    metadata={"team": "Rcb"}
)
vector_store.update_document(document_id="<doc_id>", document=update_doc1)
 
# delete
vector_store.delete(ids=["<doc_id>"])
```