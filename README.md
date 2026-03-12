# Task Manager MCP Server Integrated with Claude AI

This is MCP server built to create , update, delete tasks for daily use, and this is integrated with claude. 

You can prompt to claude ai to add,list, update and delete tasks. 

# Install fastmcp

You can install fastmcp as it is required package to build mcp servers

```bash
pip install fastmcp
```

# Run MCP Server

You can run the MCP server with the following command:

```bash
fastmcp run task_server.py
```

---

# Connect MCP Server to Claude Desktop

If you want to connect your MCP server to Claude Desktop, create a configuration file named:

`claude_desktop_config.json`

Add the following configuration:

```json
{
  "mcpServers": {
    "task_server": {
      "command": "/Users/prabhuling/work/projects/python/MCP-SERVER/mcp-app1/venv/bin/python3",
      "args": [
        "/Users/prabhuling/work/projects/python/MCP-SERVER/mcp-app1/task_server.py"
      ]
    }
  }
}
```

## Explanation

**command**  
This must point to your Python executable location (either system Python or the Python inside your virtual environment).

**args**  
This should be the full path to the Python file where your MCP server is defined.

---

# Restart Claude Desktop

After adding the configuration:

1. Quit the Claude Desktop application using **Cmd + Q**
2. Restart the application

Your MCP server will now be available to use with Claude Code.

---

# Configuration File Location

The configuration file should be located at:

```bash
~/Library/Application\ Support/Claude/claude_desktop_config.json
```

You can view it with:

```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

---

# View MCP Server Logs

To check logs for troubleshooting:

```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```