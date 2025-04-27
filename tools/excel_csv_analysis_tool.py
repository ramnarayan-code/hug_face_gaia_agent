from typing import Union
import pandas as pd

class ExcelCSVAnalysisTool:
    def analyze(self, file_path: str) -> Union[dict, str]:
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            else:
                return "Unsupported file format. Please provide a CSV or Excel file."

            # Perform analysis (e.g., summary statistics)
            summary = {
                "columns": data.columns.tolist(),
                "shape": data.shape,
                "head": data.head().to_dict(orient='records'),
                "description": data.describe(include='all').to_dict()
            }
            return summary
        except Exception as e:
            return f"An error occurred while analyzing the file: {str(e)}"