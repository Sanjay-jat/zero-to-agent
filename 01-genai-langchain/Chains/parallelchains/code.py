## Parallel chain
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model1 = ChatGoogleGenerativeAI(model=MODEL_NAME)
model2 = ChatGoogleGenerativeAI(model=MODEL_NAME)

template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="write a 2 line summary on {topic}",
    input_variables=['topic']
)

template3=PromptTemplate(
    template="merge the provided report and summary in single document \n report->{report}\n summary-> {summary}",
    input_variables=['report', 'summary']
)

parser=StrOutputParser()


parralel_chains=RunnableParallel({
    "report": template1 | model1 | parser,
    "summary": template2 | model2 | parser
})

merge_chain=template3 | model1 | parser

chains=parralel_chains | merge_chain

result=chains.invoke({"topic": "black hole"})
print(result)