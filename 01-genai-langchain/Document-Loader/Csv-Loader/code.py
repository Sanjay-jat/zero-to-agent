from langchain_community.document_loaders import CSVLoader

from dotenv import load_dotenv

load_dotenv()



loader=CSVLoader(file_path='document.csv')

docs=loader.load()

print(len(docs))

print(docs[0])

