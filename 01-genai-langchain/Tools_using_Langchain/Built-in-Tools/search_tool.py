## Search tool using langchain
from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

result=search_tool.invoke('todays headlines news')
print(result)
