import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads weather data from a CSV file, cleans it, and prepares it for modeling.
    """
    # Load the dataset
    data = pd.read_csv(filepath)
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Extract relevant features and target variable
    X = data[['temperature', 'pressure', 'humidity']]
    y = data['weather_condition']  # Example target: sunny, rainy, cloudy
    
    return X, y
