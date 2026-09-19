import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

async def main():
    client=MultiServerMCPClient({
        "practice-server-1":{
            "command":"python3",
            "args":["server.py"],
            "transport":"stdio",
        }
    })
    tools=await client.get_tools()
    # print("Tool Used By LangChain:")
    # for t in tools:
    #     print(f"Tool Name:{t.name},Tool Description:{t.description}")
    
    llm=ChatOllama(
        model="llama3.2",
        base_url="http://localhost:11434",
        temperature=0,
    )
    agent=create_agent(llm,tools)

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Answer using tools you have  What is 25 multiplied by 15?"}]}
    )

    

asyncio.run(main())
