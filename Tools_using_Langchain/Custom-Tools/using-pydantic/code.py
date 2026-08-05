from langchain_core.tools import StructuredTool

from pydantic import BaseModel ,Field

class Multiply(BaseModel):
    a:int=Field(required=True,description="first number")
    b:int=Field(required=True,description="second number")

def multiply(a:int,b:int):
    """multiply two numbers"""
    return a*b

multiply_tool=StructuredTool.from_function(
    func=multiply,
    name="multiply",    
    description="multiply two numbers",
    args_schema=Multiply
)

result=multiply_tool.invoke({"a":5,"b":10})
print(result)
