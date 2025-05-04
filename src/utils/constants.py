DEFAULT_HF_API_URL = "https://agents-course-unit4-scoring.hf.space"
GAIA_QUESTION_URL = f"{DEFAULT_HF_API_URL}/questions"
GAIA_FILE_ATTACHMENT_URL = f"{DEFAULT_HF_API_URL}/files"
REACT_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

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
IMAGE_ANALYZER_LLM = "gpt-4o"
MAIN_AGENT_LLM = "gpt-4o"