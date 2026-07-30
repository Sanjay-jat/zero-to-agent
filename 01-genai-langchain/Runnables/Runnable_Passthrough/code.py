from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough


from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write only one small joke about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='explain joke in one line only  {topic}',
    input_variables=['topic']
)

MODEL_NAME = "gemini-3.6-flash"
model =ChatGoogleGenerativeAI(model=MODEL_NAME)

parser=StrOutputParser()

generator=RunnableSequence(prompt1,model,parser)

parallel_chain =RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(generator,parallel_chain)
result=final_chain.invoke({'topic':'AI'})
print(result)