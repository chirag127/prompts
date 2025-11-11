<!-- Create a Implement a way to download the file and save it to the code baseCurrently, the extension tries to read the file and write the file itself which leading to I'm sorry. I tried to call a tool, but provided too large of an input. How would you like to proceed? create a MPC that lets the ai save a urls contents to a file in the code base. The file should be saved in the same directory as specified by the ai agent -->
create a URL Content Saver MCP Server that lets the ai agent save a urls contents to a file in the code base. The file should be saved in the same directory as specified by the ai agent. currently the ai agent is trying to read the file and write the file itself which is leading to the error as the content is too large to fit in the token limit.

Create a Model Context Protocol (MCP) Server that implements a URL Content Saver functionality. This server should:

1. Provide a tool that allows AI agents to download content from any URL and save it directly to a specified complete absolute file path in the codebase
2. Handle large content that would exceed the AI's token limit by processing the download and file writing operations server-side
3. Accept parameters including:
   - The complete URL to fetch content from (must include http:// or https://)
   - The target file path where the content should be saved
4. Support saving files to any valid path specified by the AI agent
5. Implement proper error handling for cases such as invalid URLs, network failures, or permission issues
6. Return a success confirmation or detailed error message to the AI agent

This MCP server will solve the current problem where AI agents try to read and write large files directly, which fails when the content exceeds token limits. Instead, the server will handle the data transfer without passing the content through the AI's context window.
