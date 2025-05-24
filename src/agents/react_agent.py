from langgraph.prebuilt import create_react_agent
from utils.constants import REACT_PROMPT

class ReACTAgent:
    """
    A ReACT (Reasoning and Acting) Agent implementation.
    This class implements a ReACT agent that combines reasoning and acting capabilities using
    a language model and optional tools.
    Attributes:
        agent_executor (AgentExecutor): The executor that runs the ReACT agent's reasoning and actions
    Parameters:
        llm: The language model to use for reasoning
        tools (optional): List of tools available to the agent for performing actions
    Methods:
        run(query): Execute the agent on a given query and return the result
            Args:
                query (str): The input query/prompt for the agent
            Returns:
                str: The agent's response/output for the given query
    """
    
    def __init__(self, llm, tools=None):
        self.agent = create_react_agent(model=llm, tools=tools, prompt=REACT_PROMPT)
        
    def run(self, query):
        return self.agent.invoke({"input": query})["output"]
 
