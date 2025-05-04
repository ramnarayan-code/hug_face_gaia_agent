import os
import requests
import json

from langchain_core.messages import HumanMessage
from langchain.chat_models import ChatOpenAI

from utils.image_processor import encode_image
from utils.constants import IMAGE_ANALYZER_LLM


class ImageAnalyzerTool:
    """A tool for analyzing images using OpenAI's vision model.

    This class provides functionality to analyze images by sending them to OpenAI's vision model
    along with a query/question about the image. It supports both local and remote image paths.

    Attributes:
        llm (ChatOpenAI): An instance of OpenAI's chat model configured for image analysis

    Methods:
        analyze(input_data: dict[str, str]) -> str:
            Analyzes an image based on a given query.

    Args:
        input_data (dict[str, str]): A dictionary containing:
            - image_query: The question or prompt about the image
            - image_path: URL or path to the image file

    Returns:
        str: The model's analysis/response about the image

    Raises:
        requests.exceptions.RequestException: If there's an error fetching the image
        requests.exceptions.JSONDecodeError: If there's an error decoding JSON response
        Exception: For any other unexpected errors
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            model=IMAGE_ANALYZER_LLM,
            temperature=0.0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

    def analyze(self, input_data: dict[str, str]) -> str:
        try:
            input_data = (
                json.loads(input_data) if isinstance(input_data, str) else input_data
            )

            question = input_data.get("image_query")
            image_path = input_data.get("image_path")
            if not question or not image_path:
                return "Missing image_query or image_path in input"

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

            return self.llm.invoke([message])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching audio file: {e}")
            return f"Error fetching audio file: {e}"
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON response from audio endpoint: {e}")
            return f"Error decoding JSON response from audio endpoint: {e}"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"
