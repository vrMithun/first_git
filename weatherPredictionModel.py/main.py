import data_preprocessing
import model
import plotting

def main():
    # Load and preprocess the data
    data = data_preprocessing.load_and_clean_data(r"D:\workspace\first_git\weatherPredictionModel.py\data\weather_data.csv")
    
    # Train the model
    trained_model, X_test, y_test = model.train_model(data)
    
    # Predict using the trained model
    predictions = model.predict(trained_model, X_test)
    
    # Plot the results
    plotting.plot_results(X_test, y_test, predictions)

if __name__ == "__main__":
    main()
