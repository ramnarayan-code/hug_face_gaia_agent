from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

class ReACTAgent:
    def __init__(self, llm, tools=None):
        self.react_prompt = """Answer the following questions as best you can. You have access to the following tools:

            {tools}

            Use the following format:

            Question: the input question you must answer
            Thought: you should always think about what to do
            Action: the action to take, should be one of [{tool_names}]
            Action Input: the input to the action
            Observation: the result of the action
            ... (this Thought/Action/Action Input/Observation can repeat N times)
            Thought: I now know the final answer
            Final Answer: the final answer to the original input question

            Final Answer should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. 
                    - If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. 
                    - If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. 
                    - If you are asked for a comma separated list, Apply the rules above for each element (number or string), ensure there is exactly one space after each comma.


            Begin!

            Question: {input}
            Thought:{agent_scratchpad}"""
        self.agent = create_react_agent(llm, tools, PromptTemplate.from_template(self.react_prompt))
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True, handle_parsing_errors=True)

    def run(self, query):
        return self.agent_executor.invoke({"input": query})["output"]
 