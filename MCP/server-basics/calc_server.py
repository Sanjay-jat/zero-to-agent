from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Practice Server")

@mcp.tool()
async def calculator(expression: str)->str:
    """Evaluate a basic math expression, e.g. '3*(4+5)'."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"
@mcp.tool()
async def count(text:str)->int:
    """Count the number of words in a string."""
    return len(text.split())
if __name__=="__main__":
    mcp.run()