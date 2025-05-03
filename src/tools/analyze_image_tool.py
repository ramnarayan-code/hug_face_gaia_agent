import os
import requests
import json

from typing import Union, Dict
from langchain_core.messages import HumanMessage
from langchain.chat_models import ChatOpenAI 
from utils.image_processor import encode_image

class ImageAnalyzerTool:
    def analyze(self, input_data: Union[str, Dict]):
        try:
            llm = ChatOpenAI(model="gpt-4o", temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))

            input_data = json.loads(input_data) if isinstance(input_data, str) else input_data

            question = input_data.get("image_query")
            image_path = input_data.get("image_path")
            if not question or not image_path:
                return "Missing question or image_path in input"
            
            response = requests.get(image_path, timeout=30)
            image_data = encode_image(response.content)

            message = HumanMessage(
                content=[
                    {"type": "text", "text": f"{question}"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                    },
                ]
            )
 
            return llm.invoke([message])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching audio file: {e}")
            return f"Error fetching audio file: {e}"
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON response from audio endpoint: {e}")
            return f"Error decoding JSON response from audio endpoint: {e}"
        except Exception as e:  
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"
