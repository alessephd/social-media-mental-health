# data_processing.py
import pandas as pd

def load_data(filepath):
    """Loads data from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(data):
    """Applies basic cleaning steps to the data."""
    # Example: Drop rows with missing values
    data = data.dropna()
    return data
