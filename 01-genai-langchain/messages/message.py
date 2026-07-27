from langchain.messages import AIMessage,HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

chain = model | parser
history=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Who won ipl in 2024?"),
]
answer = chain.invoke(history)
history.append(AIMessage(content=answer))

print(history)