from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Practice Server")

@mcp.tool()
async def add(a:int,b:int):
    """Add two numbers."""
    return a+b
@mcp.tool()
async def multiply(a:int,b:int):
    """Multiply two numbers."""
    return a*b

if __name__=="__main__":
    mcp.run()

