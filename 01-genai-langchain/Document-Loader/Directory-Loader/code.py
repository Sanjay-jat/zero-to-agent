from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write only one line poem on each {topic}',
    input_variables=['topic']
)


MODEL_NAME = "gemini-3.6-flash"
model =ChatGoogleGenerativeAI(model=MODEL_NAME)

parser=StrOutputParser()

loader=DirectoryLoader(path='Text_files', 
    glob="*.txt", 
    loader_cls=TextLoader, 
    loader_kwargs={'encoding':'utf-8'})

docs=loader.load()
## use lazzy loading to load the documents one by one and fastly.

print(docs[1].page_content)
print(docs[0].page_content)

print(docs[1].metadata)

# chain=prompt1 | model | parser
# result=chain.invoke({'topic':docs[0].page_content})
# print(result)