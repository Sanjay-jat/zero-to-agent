from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write only one small joke about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='define in one line only about {topic}',
    input_variables=['topic']
)

MODEL_NAME = "gemini-3.6-flash"
model =ChatGoogleGenerativeAI(model=MODEL_NAME)

parser=StrOutputParser()

parallel_chain =RunnableParallel({
    'joke':RunnableSequence(prompt1,model,parser),
    'definition':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'AI'})
print(result)