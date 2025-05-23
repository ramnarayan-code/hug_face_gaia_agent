# LangChain ReACT Agent with Multi-Tool Support

## Overview
This project implements a ReACT agent using LangChain framework, equipped with multiple tools for information retrieval, data analysis, and media processing. The agent combines Wikipedia searches, file analysis, and audio transcription capabilities to provide comprehensive information processing.

## Features
- Wikipedia article search and summary retrieval
- Excel/CSV file analysis with statistical insights
- Audio transcription from files and URLs using Whisper
- ReACT-based reasoning for complex queries
- In-memory file processing for efficient operations

## Project Structure
```
src/
├── tools/ (LLM Tools)
├── agents/ (ReACT agent)
└── utils/ (Utility functions)
```
## Streamable-http MCP Client and MCP Server
1. Start MCP Server
```
python src/setup_mcp_server.py
```
2. Start MCP Client
```
python src/hugging_face_app_with_remote_mcp.py
```
Source code: [GAIA Agent](https://github.com/ramnarayan-code/hug_face_gaia_agent)
