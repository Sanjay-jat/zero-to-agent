from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate

load_dotenv()

video_id = "_6R7Ym6Vy_I"

try:
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=["en"])
    text = " ".join(snippet.text for snippet in transcript)

except TranscriptsDisabled:
    print("Transcript is disabled for this video.")
    exit()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.create_documents([text])

print(f"Total Chunks: {len(chunks)}")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print(f"Stored Documents: {vector_store._collection.count()}")

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not present in the context, simply say:
"I don't know."

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

question = input("Enter your question: ")

docs = retriever.invoke(question)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 80)
    print(f"Chunk {i}")
    print(doc.page_content[:400])

context = "\n\n".join(doc.page_content for doc in docs)

final_prompt = prompt.invoke(
    {
        "context": context,
        "question": question
    }
)

response = llm.invoke(final_prompt)

print("\nAnswer:\n")
print(response.content[0]["text"])


## using chains 
# from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableSequence

# def format_docs(docs):
#     context_text = "\n\n".join(doc.page_content for doc in docs)
#     return context_text

# parallel_chain=RunnableParallel({
#     'context':retriever|RunnableLambda(format_docs),
#     'question':RunnablePassthrough()
# })
# print(parallel_chain.invoke('what is generative AI?'))

# parser=StrOutParser()

# main_chain=parallel_chain|prompt|llm|parser

# main_chain.invoke('what is generative AI?')
