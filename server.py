from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Tools")

@mcp.tool()
def greeting(name: str)-> str:
    """
    Returns a greeting message for the given name.
    Args:
        name: The name of the person to greet.
    """
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

