from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)
parser=JsonOutputParser()

template1=PromptTemplate(
    template="write a 5 facts on {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


chain=template1 | model | parser

result=chain.invoke({"topic": "criket"})
print(result)