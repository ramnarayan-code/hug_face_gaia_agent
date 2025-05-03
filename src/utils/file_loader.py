def load_excel_file(file_path):
    import pandas as pd
    return pd.read_excel(file_path)

def load_csv_file(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def parse_data(data_frame):
    return data_frame.describe()  # Returns a summary of the DataFrame

def load_file(file_path, file_type=None):
    if file_type == 'xlsx':
        return load_excel_file(file_path)
    elif file_type == 'csv':
        return load_csv_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide an Excel or CSV file.")