from langchain_core.tools import tool

@tool
def multiply(a:int ,b:int):
    """multiply two numbers"""
    return a*b

result=multiply.invoke({"a":5,"b":10})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)