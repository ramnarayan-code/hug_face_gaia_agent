import requests
import construct_react_agent


DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
api_url = DEFAULT_API_URL
questions_url = f"{api_url}/questions"
file_url = f"{api_url}/files"

try:
   

    question = "The attached Excel file contains the sales of menu items for a local fast-food chain. What were the total sales that the chain made from food (not including drinks)? Express your answer in USD with two decimal places."

    agent = construct_react_agent.get_react_agent()
    agent.run(f"{question} file_url: {file_url}/7bd855d8-463d-4ed5-93ca-5fe35145f733 file_type: xlsx")
except requests.exceptions.RequestException as e:
    print(f"Error fetching questions: {e}")
except requests.exceptions.JSONDecodeError as e:
    print(f"Error decoding JSON response from questions endpoint: {e}")
    print(f"Response text: {response.text[:500]}")
except Exception as e:
    print(f"An unexpected error occurred fetching questions: {e}")
