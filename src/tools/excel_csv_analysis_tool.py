import pandas as pd
import requests
import json

from io import BytesIO
from urllib.parse import urlparse
from utils.file_loader import load_file, describe_data

class ExcelCSVAnalysisTool:
    """Excel and CSV Analysis Tool for data processing and basic statistical analysis.
    This class provides functionality to analyze Excel and CSV files, either from local sources
    or remote URLs. It performs basic statistical analysis and provides a summary of the data.
    Attributes:
        None
    Methods:
        _download_file(url: str) -> BytesIO:
            Downloads a file from the given URL and returns it as a BytesIO object.
        __get_file_object(file_source: str, file_type: str) -> tuple[BytesIO | str, str]:
            Processes the file source and returns a tuple containing the file object and its type.
        analyze(input_data: str | dict) -> dict | str:
            Analyzes the input file and returns a dictionary containing basic statistical information
            or an error message if the analysis fails.
    Example:
        >>> tool = ExcelCSVAnalysisTool()
        >>> result = tool.analyze({
        ...     'file_url': 'https://example.com/data.csv',
        ...     'file_type': 'csv'
        ... })
        >>> print(result)  # Prints analysis summary
    Notes:
        - Supported file types include Excel (.xlsx, .xls) and CSV files
        - Input can be either a JSON string or a dictionary
        - The analysis includes column names, data shape, head of the dataset, and statistical description
    """
    
    def _download_file(self, url: str) -> BytesIO:
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to download file: {str(e)}")

    def __get_file_object(self, file_source: str, file_type: str) -> BytesIO | str:
        file_type = file_type.lower() if file_type != "" else urlparse(file_source).path.lower()
        if file_source.startswith(('http://', 'https://')):
            print(f"Downloading file from URL: {file_source}")
            file_obj = self._download_file(file_source)
        else:
            file_obj = file_source
            
        return file_obj, file_type
    
    def analyze(self, input_data: str | dict) -> dict | str:
        try:
            # Handle dictionary input
            input_data = json.loads(input_data) if isinstance(input_data, str) else input_data

            file_source = input_data.get('file_url')
            file_type = input_data.get('file_type', '')
            if not file_source:
                return "Missing file_source in input"

            file_obj, file_type = self.__get_file_object(file_source, file_type)
            data = load_file(file_obj, file_type)

            # Perform analysis
            summary = {
                "columns": data.columns.tolist(),
                "shape": data.shape,
                "head": data.head().to_dict(orient='records'),
                "description": describe_data(data, "all").to_dict()
            }
            return summary
        except Exception as e:
            return f"An error occurred while analyzing the file: {str(e)}"