from scripts.data_preprocessing import load_and_clean_data, add_lag_features, scale_data
from scripts.visualization import plot_temperature_trend
from scripts.model_training import train_model

def main():
    # Step 1: Load and preprocess data
    file_path = "d:/workspace/first_git/basicWeatherPrediction.py/data/weather_data.csv"

    df = load_and_clean_data(file_path)
    df = add_lag_features(df)
    df, scaler = scale_data(df)
    
    # Step 2: Visualize data
    plot_temperature_trend(df)
    
    # Step 3: Train model
    model = train_model(df)
    
    print("Model training completed!")
    
if __name__ == "__main__":
    main()
