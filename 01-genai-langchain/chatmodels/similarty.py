from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

docs = [
    "Virat Kohli is one of India's greatest batsmen and a former cricket captain.",
    "Jasprit Bumrah is India's premier fast bowler known for his deadly yorkers.",
    "Sachin Tendulkar is regarded as one of the greatest cricketers in the history of the game.",
    "MS Dhoni is a legendary Indian wicketkeeper-batsman known for his calm leadership and finishing skills."
]

query="tell me about jasprit yorkers"

embedded_docs=embeddings.embed_documents(docs)
embedded_query=embeddings.embed_query(query)

scores=cosine_similarity([embedded_query],embedded_docs)[0]
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print(score)