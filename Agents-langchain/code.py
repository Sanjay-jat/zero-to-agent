from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
import requests
import os
API_KEY = os.getenv("API_KEY")

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",   # gemini-3.5-flash doesn't exist
    temperature=0,
)

search_tool = DuckDuckGoSearchRun()
@tool
def weather_tool(city:str)->str:
    """
    Get the current weather for a given city.
    """
    url = f"https://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    return response.json()

agent = create_agent(
    model=llm,
    tools=[search_tool, weather_tool],
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "capital of Rajasthan and the current weather there"
            }
        ]
    }
)

print(response["messages"][-1].content[0]["text"])