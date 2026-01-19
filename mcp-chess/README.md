# Installation Steps

To install the MCP server, add this code to your JSON config file

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "uvx",
      "args": [
        "--from",
        "git+ ",
        "chess"
      ]
    }
  }
}
```
