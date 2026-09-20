from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Practice Server")



@mcp.resource("greeting://hello")
async def get_greeting() -> str:
    """A simple static greeting resource."""
    return "Hello from the MCP server. This is a resource, not a tool."

@mcp.tool()
async def add(a:int,b:int):
    """Add two numbers."""
    return a+b


if __name__=="__main__":
    mcp.run()


