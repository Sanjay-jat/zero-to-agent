from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


@tool
def multiply(a:int ,b:int):
    """multiply two numbers"""
    return a*b


llm_max=llm.bind_tools([multiply])

query=HumanMessage(content="multiply 5 and 6")  

messages=[query]

result=llm_max.invoke(messages)
messages.append(result)

tool_result=multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

llm_result=llm_max.invoke(messages)
print("final result-:", llm_result.content[0]["text"])