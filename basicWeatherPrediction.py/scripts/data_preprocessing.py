import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_clean_data(file_path):
    # Load data
    df = pd.read_csv(file_path, parse_dates=['Date'])
    
    # Sort by date
    df.sort_values(by='Date', inplace=True)
    
    # Handle missing values (e.g., fill with mean)
    df['Temperature'].fillna(df['Temperature'].mean(), inplace=True)
    
    return df

def add_lag_features(df):
    # Add lag feature (yesterday's temperature)
    df['Temp_Yesterday'] = df['Temperature'].shift(1)
    df.dropna(inplace=True)  # Remove rows with NaN after shifting
    return df

def scale_data(df):
    scaler = MinMaxScaler()
    df[['Temperature', 'Temp_Yesterday']] = scaler.fit_transform(df[['Temperature', 'Temp_Yesterday']])
    return df, scaler
