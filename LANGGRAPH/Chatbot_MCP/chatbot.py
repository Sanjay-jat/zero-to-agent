from typing import TypedDict, Annotated, Literal
import sqlite3
from langgraph import graph
import requests

from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
load_dotenv()
import os
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://172.31.0.1:11434"
)

client=MultiServerMCPClient(
    {
        "arith":{
            "transport":"stdio",
            "command":"python3",
            "args":["server.py"],
        }
    }
    
)

class Chat(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


async def build_graph():
    tools=await client.get_tools()
    llm_with_tools=llm.bind_tools(tools)
    async def chat_node(State:Chat):
        messages = State["messages"]
        response = await llm_with_tools.ainvoke(messages)
        return {"messages":response}
    tool_node=ToolNode(tools)
    graph = StateGraph(Chat)
    graph.add_node("chat", chat_node)
    graph.add_node("tools", tool_node)
    graph.add_edge(START, "chat")
    graph.add_conditional_edges(
        "chat",
        tools_condition,
        {
            "tools": "tools",
            "__end__": END
        }
    )
    graph.add_edge("tools", "chat")
    chatbot = graph.compile()
    return chatbot


async def main():
    chatbot=await build_graph()
    result=await chatbot.ainvoke({"messages":[SystemMessage(content="You are a helpful assistant."),HumanMessage(content="heyy my name is sanjay can you multiply 300 with 40 and then add 1000 to the ans you can use the tool and i you use them pls tell me ")]})
    print(result['messages'][-1].content)
if __name__=='__main__':
    asyncio.run(main())
