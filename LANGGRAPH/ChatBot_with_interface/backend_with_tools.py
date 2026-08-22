from typing import TypedDict, Annotated, Literal
import sqlite3
import requests

from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()
import os
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://172.31.0.1:11434"
)


class Chat(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


class Router(BaseModel):
    tool: Literal["none", "calculator", "search", "stock"]


router = llm.with_structured_output(Router)


@tool
def calculator(first_num: float, second_num: float, operation: str):
    """Perform add, subtract, multiply or divide."""

    if operation == "add":
        result = first_num + second_num

    elif operation == "subtract":
        result = first_num - second_num

    elif operation == "multiply":
        result = first_num * second_num

    elif operation == "divide":
        if second_num == 0:
            return {"error": "Cannot divide by zero"}
        result = first_num / second_num

    else:
        return {"error": "Invalid operation"}

    return {
        "first_num": first_num,
        "second_num": second_num,
        "operation": operation,
        "result": result
    }


@tool
def get_stocks_price(symbol: str):
    """Get stock price for a stock symbol."""

    url = (
        "https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE"
        f"&symbol={symbol.upper()}"
        f"&apikey={api_key}"
    )

    return requests.get(url).json()


search_tool = DuckDuckGoSearchRun(region="us-en")

tools = [
    calculator,
    search_tool,
    get_stocks_price
]


def chat_node(state: Chat):

    messages = state["messages"]

    decision = router.invoke([
        SystemMessage(content="""
Decide whether the user's latest message needs a tool.

Return:
- none = normal conversation, greetings, explanations, coding questions
- calculator = arithmetic
- search = current, recent or web information
- stock = stock price or stock information

Never use a tool for greetings or casual conversation.
"""),
        messages[-1]
    ])

    if decision.tool == "none":

        response = llm.invoke(messages)

        return {
            "messages": [response]
        }

    llm_tools = llm.bind_tools(tools)

    response = llm_tools.invoke(messages)

    return {
        "messages": [response]
    }


tool_node = ToolNode(tools)


conn = sqlite3.connect(
    "chatbot.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn)


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

chatbot = graph.compile(
    checkpointer=checkpointer
)


def retrieve_all_threads():

    threads = set()

    for check in checkpointer.list(None):
        threads.add(
            check.config["configurable"]["thread_id"]
        )

    return list(threads)