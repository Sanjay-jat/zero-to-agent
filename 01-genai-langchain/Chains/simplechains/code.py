##simple chain 
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)

template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="write a 5 line summary on {text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic": "black hole"})
print(result)