from langchain_classic.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)

class Person(BaseModel):
    name:str
    age:int

parser=PydanticOutputParser(pydantic_object=Person)


template1=PromptTemplate(
    template="write name and age of best batman of indian odi cricket team \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


chain=template1 | model | parser

result=chain.invoke({})
print(result)