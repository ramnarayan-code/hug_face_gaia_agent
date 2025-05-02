import requests
import construct_react_agent


DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
api_url = DEFAULT_API_URL
questions_url = f"{api_url}/questions"
file_url = f"{api_url}/files"


def test_excel():
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

def test_audio():
    try:
        question = """Hi, I was out sick from my classes on Friday, so I'm trying to figure out what I need to study for my Calculus mid-term next week. My friend from class sent me an audio recording of Professor Willowbrook giving out the recommended reading for the test, but my headphones are broken :(
Could you please listen to the recording for me and tell me the page numbers I'm supposed to go over? I've attached a file called Homework.mp3 that has the recording. Please provide just the page numbers as a comma-delimited list. And please provide the list in ascending order."""

        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question} audio_path: {file_url}/1f975693-876d-457b-a649-393859e79bf3")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")


def test_libre():
    try:
        question = """What is the surname of the equine veterinarian mentioned in 1.E Exercises from the chemistry materials licensed by Marisa Alviar-Agnew & Henry Agnew under the CK-12 license in LibreText's Introductory Chemistry materials as compiled 08/21/2023?"""
        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")



def test_grocery():
    try:
        question = """I'm making a grocery list for my mom, but she's a professor of botany and she's a real stickler when it comes to categorizing things. I need to add different foods to different categories on the grocery list, but if I make a mistake, she won't buy anything inserted in the wrong category. Here's the list I have so far:

milk, eggs, flour, whole bean coffee, Oreos, sweet potatoes, fresh basil, plums, green beans, rice, corn, bell pepper, whole allspice, acorns, broccoli, celery, zucchini, lettuce, peanuts

I need to make headings for the fruits and vegetables. Could you please create a list of just the vegetables from my list? If you could do that, then I can figure out how to categorize the rest of the list into the appropriate categories. But remember that my mom is a real stickler, so make sure that no botanical fruits end up on the vegetable list, or she won't get them when she's at the store. Please alphabetize the list of vegetables, and place each item in a comma separated list."""
        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")

def test_shopping_audio():
    try:
        question = """Hi, I'm making a pie but I could use some help with my shopping list. I have everything I need for the crust, but I'm not sure about the filling. I got the recipe from my friend Aditi, but she left it as a voice memo and the speaker on my phone is buzzing so I can't quite make out what she's saying. Could you please listen to the recipe and list all of the ingredients that my friend described? I only want the ingredients for the filling, as I have everything I need to make my favorite pie crust. I've attached the recipe as Strawberry pie.mp3.

In your response, please only list the ingredients, not any measurements. So if the recipe calls for ""a pinch of salt"" or ""two cups of ripe strawberries"" the ingredients on the list would be ""salt"" and ""ripe strawberries"".

Please format your response as a comma separated list of ingredients. Also, please alphabetize the ingredients."""
        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question} audio_path: {file_url}/99c9cc74-fdc8-46c6-8f8d-3ce2d3bfeea3")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")

def test_polish():
    try:
        question = """Who did the actor who played Ray in the Polish-language version of Everybody Loves Raymond play in Magda M.? Give only the first name."""
        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")

def test_py():
    try:
        question_text = "What is the final numeric output from the attached Python code?"
        response = requests.get(f"{file_url}/f918266a-b3e0-4914-865d-4faa564f1aef", timeout=30)
        question_text = f"{question_text} Python program: {response.content}"
        agent = construct_react_agent.get_react_agent()
        agent.run(f"{question_text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response from questions endpoint: {e}")
        print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred fetching questions: {e}")

# test_excel()
# test_audio()
# test_libre()
# test_grocery()
# test_shopping_audio()
# test_polish()
test_py()