from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import re
from langchain_ollama import ChatOllama
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3 
from langgraph.graph import add_messages
import operator
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import BaseMessage
from typing import Literal
from pydantic import Field,BaseModel
## tools import
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests

load_dotenv()

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://172.31.0.1:11434"
)
class Chat(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
## tools
search_tool = DuckDuckGoSearchRun(region='us-en')
@tool
def calculator(first_num:float,second_num:float,operation:str)->dict:
    """
    A simple calculator tool that performs basic arithmetic operations on two numbers.
    Supported operations: add, subtract, multiply, divide
    """
    try:
        
        if operation == 'add':
            result = first_num + second_num
        elif operation == 'subtract':
            result = first_num - second_num
        elif operation == 'multiply':
            result = first_num * second_num
        elif operation == 'divide':
            if second_num == 0:
                return {"error": "Division by zero is not allowed."}
            result = first_num / second_num
        return {'first_num': first_num, 'second_num': second_num, 'operation': operation, 'result': result}
    except Exception as e:
        return {"error": str(e)}

@tool
def get_stocks_price(symbol:str)->dict:
    """
    A tool to get stock price for a given stock symbol {eg-AAPL,GOOGL,MSFT,TSLA,AMZN}
    using alpha vantage with api key in the url
    """
    url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=demo"
    r=requests.get(url)
    return r.json()
## tools binding 
tools=[search_tool,calculator,get_stocks_price]
llm_with_tools = llm.bind_tools(tools)
SYSTEM_PROMPT = """
You are a helpful assistant.

Rules:
- Never call tools for greetings, small talk, or casual conversation.
- Use the calculator tool only for arithmetic requests.
- Use the web search tool only for live or current information.
- Use the stock tool only for stock symbol price requests.
- If no tool is required, answer normally in plain conversation.
"""

def chat_node(state:Chat):
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {'messages': [response]}

tool_node = ToolNode(tools)

## db connection
conn=sqlite3.connect('chatbot.db',check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

##workflow graph
graph = StateGraph(Chat)
graph.add_node('chat_node',chat_node)
graph.add_node('tools',tool_node)
graph.add_edge(START,'chat_node')
graph.add_conditional_edges('chat_node',tools_condition)
graph.add_edge('tools','chat_node')

chatbot=graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads=set()
    for check in checkpointer.list(None):
        all_threads.add(check.config['configurable']['thread_id'])
    return list(all_threads)
