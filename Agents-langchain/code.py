from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",   # gemini-3.5-flash doesn't exist
    temperature=0,
)

search_tool = DuckDuckGoSearchRun()

agent = create_agent(
    model=llm,
    tools=[search_tool],
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "3 ways to reach Goa from Rajasthan"
            }
        ]
    }
)

print(response["messages"][-1].content[0]["text"])