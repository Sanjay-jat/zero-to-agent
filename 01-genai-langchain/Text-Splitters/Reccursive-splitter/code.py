from langchain_text_splitters import RecursiveCharacterTextSplitter

text="This is a sample text that we will use to demonstrate the functionality of the RecursiveCharacterTextSplitter. The splitter will divide this text into smaller chunks based on the specified chunk size and overlap. Each chunk will be separated by a period, and we will see how the text is split accordingly."

splitter=RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)

splits=splitter.split_text(text)
print(splits)
print(len(splits))