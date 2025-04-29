from typing import Union, Dict
import pandas as pd
import requests
from io import BytesIO
from urllib.parse import urlparse
import json

class ExcelCSVAnalysisTool:
    def _download_file(self, url: str) -> BytesIO:
        """Downloads file from URL and returns BytesIO object."""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to download file: {str(e)}")

    def analyze(self, input_data: Union[str, Dict]) -> Union[dict, str]:
        """
        Analyzes Excel or CSV files from URL or local path.
        
        Args:
            input_data: Either a string URL/path or a dictionary with file_url and file_type
        """
        try:
            # Handle dictionary input
            input_data = json.loads(input_data) if isinstance(input_data, str) else input_data
            file_source = input_data.get('file_url')
            file_type = input_data.get('file_type', '')
            if not file_source:
                return "Missing file_source in input"

            # Check if the source is a URL
            if file_source.startswith(('http://', 'https://')):
                print(f"Downloading file from URL: {file_source}")
                file_obj = self._download_file(file_source)
                # Use provided file_type or try to determine from URL
                file_extension = file_type.lower() if file_type else urlparse(file_source).path.lower()
            else:
                file_obj = file_source
                file_extension = file_source.lower()

            print(f"File extension: {file_extension}")
            # Read the file into pandas
            if 'csv' in file_extension:
                data = pd.read_csv(file_obj if isinstance(file_obj, BytesIO) else file_obj)
            elif 'xlsx' in file_extension:
                data = pd.read_excel(file_obj if isinstance(file_obj, BytesIO) else file_obj)
            else:
                return "Unsupported file format. Please provide a CSV or Excel file."

            # Perform analysis
            summary = {
                "columns": data.columns.tolist(),
                "shape": data.shape,
                "head": data.head().to_dict(orient='records'),
                "description": data.describe(include='all').to_dict()
            }
            return summary
        except Exception as e:
            return f"An error occurred while analyzing the file: {str(e)}"