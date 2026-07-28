from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)
schema=[
    ResponseSchema(name="fact1",description="fact 1 about the topic"),
    ResponseSchema(name="fact2",description="fact 2 about the topic"),
]
parser=StructuredOutputParser.from_response_schemas(schema)


template1=PromptTemplate(
    template="write a 2 facts on {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


chain=template1 | model | parser

result=chain.invoke({"topic": "criket"})
print(result)