from langchain_community.tools import ShellTool

shell=ShellTool()

results=shell.invoke('ls')
print(results)