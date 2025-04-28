import os

from langchain.chat_models import ChatOpenAI  
from langchain.agents import Tool

from agents.react_agent import ReACTAgent
from tools.wikipedia_tool import WikipediaTool
from tools.excel_csv_analysis_tool import ExcelCSVAnalysisTool
from tools.transcribe_audio_tool import AudioTranscriberTool
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["OPENAI_API_KEY"] = ""
os.environ["TAVILY_API_KEY"] = ""

def main():
  
    llm = ChatOpenAI(model="gpt-o4-mini", temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    tools = [
        TavilySearchResults(max_results=1),
        Tool(name="Wikipedia", func=WikipediaTool().search, description="Search for information on Wikipedia."),
        Tool(name="Excel/CSV Analysis", func=ExcelCSVAnalysisTool().analyze, description="Analyze Excel and CSV files."),
        Tool(name="Transcribe audio", func=AudioTranscriberTool().process_speech_to_text, description="Analyze Excel and CSV files."),
    ]

    # Initialize the ReACT agent with the tools
    agent = ReACTAgent(llm=llm, tools=tools)
       
    # Start the agent to process user queries
    question = "How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia."
    response = agent.run(question)
    print(f"Question: {question}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
