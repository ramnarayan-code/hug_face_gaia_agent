import os

from langchain.chat_models import ChatOpenAI  
from langchain.agents import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL

from agents.react_agent import ReACTAgent
from tools.wikipedia_tool import WikipediaTool
from tools.excel_csv_analysis_tool import ExcelCSVAnalysisTool
from tools.transcribe_audio_tool import AudioTranscriberTool
from tools.analyze_image_tool import ImageAnalyzerTool
from tools.analyze_yt_video_tool import AnalyzeYTVideoTool
from utils.constants import MAIN_AGENT_LLM

def get_chatbot() -> ReACTAgent:
  
    llm = ChatOpenAI(model=MAIN_AGENT_LLM, temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    tools = [
        TavilySearchResults(max_results=3),
        Tool(name="python_repl", func=PythonREPL().run, description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",),
        Tool(name="Wikipedia", func=WikipediaTool().search, description="Search for information on Wikipedia."),
        Tool(name="Excel/CSV Analysis", func=ExcelCSVAnalysisTool().analyze, description="Analyze Excel and CSV files."),
        Tool(name="Transcribe audio", func=AudioTranscriberTool().transcribe_audio_from_url, description="Analyze Excel and CSV files."),
        Tool(name="Analyze image", func=ImageAnalyzerTool().analyze, description="Analyze image and desribe it in concise manner."),
        Tool(name="Analyze Youtube Video", func=AnalyzeYTVideoTool().analyze, description="Analyze Youtube video and transcribe it to text."),
    ]

    # Initialize the ReACT agent with the tools
    agent = ReACTAgent(llm=llm, tools=tools)
       
    return agent

