import os

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

class ReACTAgent:
    def __init__(self, llm, tools=None):
        self.react_prompt = hub.pull("hwchase17/react")
        self.agent = create_react_agent(llm, tools, self.react_prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)

    def run(self, query):
        return self.agent_executor.invoke({"input": query})["output"]
