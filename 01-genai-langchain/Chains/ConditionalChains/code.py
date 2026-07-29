## Conditional chains
from langchain_classic.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)

class feedback(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="sentiment of the input text in positive or negative only")

parser=PydanticOutputParser(pydantic_object=feedback)


template1=PromptTemplate(
    template="sentiment of the input text in positive or negative only \n {feedback}\n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


classifier_chain=template1 | model | parser

template2=PromptTemplate(
    template="write an appropriate response to the positive feedback  \n {feedback}",
    input_variables=['feedback'],
)
template3=PromptTemplate(
    template="write an appropriate response to the negative feedback  \n {feedback}",
    input_variables=['feedback'],
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",template2|model|parser),
    (lambda x:x.sentiment=="negative",template3|model|parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chains=classifier_chain | branch_chain

result=chains.invoke({"feedback": "I love the new features of your product!"})
print(result)
