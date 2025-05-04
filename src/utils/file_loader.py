import pandas as pd

def load_excel_file(file_path):
    """
    Load data from an Excel file into a pandas DataFrame.

    Args:
        file_path (str): Path to the Excel file to be loaded.

    Returns:
        pandas.DataFrame: DataFrame containing the Excel file data.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        pd.errors.EmptyDataError: If the Excel file is empty.
        pd.errors.ParserError: If the file cannot be parsed as an Excel file.
    """
    return pd.read_excel(file_path)

def load_csv_file(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file to be loaded.

    Returns:
        pandas.DataFrame: DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        pandas.errors.EmptyDataError: If the CSV file is empty.
        pandas.errors.ParserError: If the file cannot be parsed as a CSV.
    """
    return pd.read_csv(file_path)

def describe_data(data_frame, include=None):
    """
    Generate descriptive statistics for a pandas DataFrame.
    This function provides statistical information about numerical and/or categorical columns
    in the DataFrame using pandas' describe() method.
    Args:
        data_frame (pandas.DataFrame): The DataFrame to analyze
        include (list or None, optional): A list of data types to include in the analysis. 
            If None, only numeric columns are included. Defaults to None.
    Returns:
        pandas.DataFrame: A DataFrame containing descriptive statistics including:
            - For numeric data: count, mean, std, min, 25%, 50%, 75%, max
            - For object data (if included): count, unique, top, freq
    Example:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        >>> describe_data(df, include=['number', 'object'])
    """
    return data_frame.describe(include=include)  # Returns a summary of the DataFrame

def load_file(file_path, file_type=None):
    """
    Load a file from the specified file path.

    This function supports loading Excel (.xlsx) and CSV files.

    Args:
        file_path (str): Path to the file to be loaded
        file_type (str, optional): Type of file to load ('xlsx' or 'csv'). 
            If not specified, will raise an error.

    Returns:
        pandas.DataFrame: The loaded file data as a DataFrame

    Raises:
        ValueError: If the file_type is not supported (must be 'xlsx' or 'csv')

    Examples:
        >>> df = load_file('data.xlsx', 'xlsx')
        >>> df = load_file('data.csv', 'csv')
    """
    if file_type == 'xlsx':
        return load_excel_file(file_path)
    elif file_type == 'csv':
        return load_csv_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide an Excel or CSV file.")