from typing import Optional
from mcp.server.fastmcp import FastMCP    

from langchain_community.tools.tavily_search import TavilySearchResults
from tools.excel_csv_analysis_tool import ExcelCSVAnalysisTool
from tools.transcribe_audio_tool import AudioTranscriberTool
from tools.wikipedia_tool import WikipediaTool
from tools.analyze_image_tool import ImageAnalyzerTool
from tools.analyze_yt_video_tool import AnalyzeYTVideoTool

mcp = FastMCP("My App")

@mcp.tool()
def search_in_tavily(query: Optional[str] = None):
    return TavilySearchResults().invoke({'query': query})

@mcp.tool()
def analyze_csv(input_data: str | dict):
    return ExcelCSVAnalysisTool().analyze(input_data)

@mcp.tool()
def transcribe_audio(audio_file_url: str):
    return AudioTranscriberTool().transcribe_audio_from_url(audio_file_url)

@mcp.tool()
def search_in_wiki(query: str):
    return WikipediaTool().search(query)

@mcp.tool()
def analyze_image(input_data: dict[str, str]):
    return ImageAnalyzerTool().analyze(input_data)

@mcp.tool()
def analyze_yt(url: str):
    return AnalyzeYTVideoTool().analyze(url)

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")
