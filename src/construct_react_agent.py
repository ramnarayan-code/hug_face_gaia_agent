import os

from langchain.chat_models import ChatOpenAI  
from langchain.agents import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL


from agents.react_agent import ReACTAgent
from tools.wikipedia_tool import WikipediaTool
from tools.excel_csv_analysis_tool import ExcelCSVAnalysisTool
from tools.transcribe_audio_tool import AudioTranscriberTool


def get_react_agent() -> ReACTAgent:
  
    llm = ChatOpenAI(model="gpt-o4-mini", temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    tools = [
        TavilySearchResults(max_results=1),
        Tool(name="python_repl", func=PythonREPL().run, description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",),
        Tool(name="Wikipedia", func=WikipediaTool().search, description="Search for information on Wikipedia."),
        Tool(name="Excel/CSV Analysis", func=ExcelCSVAnalysisTool().analyze, description="Analyze Excel and CSV files."),
        Tool(name="Transcribe audio", func=AudioTranscriberTool().process_speech_to_text, description="Analyze Excel and CSV files."),
    ]

    # Initialize the ReACT agent with the tools
    agent = ReACTAgent(llm=llm, tools=tools)
       
    return agent

<<<<<<< HEAD:src/construct_react_agent.py
=======
if __name__ == "__main__":
    main()
>>>>>>> 2af69503c3b8ed148b8ce34af296cc451964fefa:main.py
