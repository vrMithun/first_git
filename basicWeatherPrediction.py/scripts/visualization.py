import matplotlib.pyplot as plt

def plot_temperature_trend(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Temperature'], label='Temperature')
    plt.title('Temperature Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()
