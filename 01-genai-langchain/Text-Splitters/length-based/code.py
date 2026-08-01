# from langchain_text_splitters import CharacterTextSplitter

# text="This is a sample text that we will use to demonstrate the functionality of the CharacterTextSplitter. The splitter will divide this text into smaller chunks based on the specified chunk size and overlap. Each chunk will be separated by a period, and we will see how the text is split accordingly."

# splitter=CharacterTextSplitter(chunk_size=50, chunk_overlap=10,separator=".")

# splits=splitter.split_text(text)
# print(splits)

## now using textloader to load the text from a file and then split it using CharacterTextSplitter

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader('document.txt',encoding='utf-8')

docs=loader.load()

splitter=CharacterTextSplitter(chunk_size=50, chunk_overlap=10,separator=".")

splits=splitter.split_documents(docs)
print(splits[0].page_content)