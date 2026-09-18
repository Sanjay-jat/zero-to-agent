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
@mcp.resource("greeting://hello")
async def get_greeting() -> str:
    """A simple static greeting resource."""
    return "Hello from the MCP server. This is a resource, not a tool."

@mcp.resource("user://{name}")
async def get_user_info(name: str) -> str:
    """Get info about a specific user by name."""
    return f"User profile for {name}: this is a placeholder user record." 

@mcp.prompt()
async def math_explainer(number: str) -> str:
    """Generate a prompt asking to explain a number's properties."""
    return f"Explain the mathematical properties of the number {number} in simple terms."

if __name__=="__main__":
    mcp.run()


