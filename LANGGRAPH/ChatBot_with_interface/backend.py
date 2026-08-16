from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
import operator
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
load_dotenv()

from typing import Literal
from pydantic import Field,BaseModel
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://172.31.0.1:11434"
)

class Chat(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state:Chat):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

checkpointer = InMemorySaver()
graph = StateGraph(Chat)
graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)
chatbot=graph.compile(checkpointer=checkpointer)