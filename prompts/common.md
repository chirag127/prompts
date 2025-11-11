"""
Common Prompt Patterns (common.md)

Purpose:
    Reusable prompt components and patterns for consistent AI interactions.
    Contains standard instructions for documentation gathering, tool usage, and output formatting.

Usage:
    Include these patterns in custom prompts to ensure consistent behavior and proper tool usage.

Author: Chirag Singhal (@chirag127)
"""

Please use the available tools to gather comprehensive documentation for this project:

1. Use the `web-search` tool to find relevant documentation about YouTube API, browser extensions, and Gemini API integration.
2. Use `web-fetch` to retrieve specific documentation pages once you've identified them.
3. Utilize the `context7` MCP server to pull up-to-date, version-specific documentation for key libraries and frameworks we'll be using.
4. Apply `Stochastic Thinking MCP Server and clear thought mcp server` to analyze the gathered information and extract key insights.

Please organize your findings in a structured way.