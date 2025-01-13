import matplotlib.pyplot as plt

def plot_results(X_test, y_test, predictions):
    """
    Display the results of the predictions.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(y_test, label="Actual Values", marker="o", linestyle="-")
    plt.plot(predictions, label="Predicted Values", marker="x", linestyle="--")
    plt.xlabel("Sample Index")
    plt.ylabel("Weather Parameter Value")
    plt.title("Weather Prediction Results")
    plt.legend()
    plt.grid(True)
    plt.show()  # Directly display the plot
