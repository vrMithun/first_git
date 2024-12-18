import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# File path
file_path = r"D:\workspace\first_git\weatherPredictionModel.py\data\data.csv"

# Load the data
df = pd.read_csv(file_path)

# Drop unnecessary columns
columns_to_remove = [
    'Summary', 'Precip Type', 'Apparent Temperature (C)', 'Humidity',
    'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover',
    'Pressure (millibars)', 'Daily Summary', 'Wind Speed (km/h)'
]
df = df.drop(columns=columns_to_remove)

# Convert 'Formatted Date' to datetime (timezone-aware)
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)

# Filter data for December 2015
df_year= df[df['Formatted Date'].dt.year == 2015]
df_year_month = df_year[df_year['Formatted Date'].dt.month == 12]

# Convert 'Formatted Date' to a numeric format for regression
df_year_month['Date Numeric'] = df_year_month['Formatted Date'].view('int64')  # Converts to the number of nanoseconds since epoch

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df_year_month['Date Numeric'], df_year_month['Temperature (C)'])

# Define the linear model
def myfunc(x):
    return slope * x + intercept

# Apply the linear model to the numeric dates
mymodel = list(map(myfunc, df_year_month['Date Numeric']))

# Plot the scatter plot and the regression line
#plt.figure(figsize=(10, 6))
plt.scatter(df_year_month['Formatted Date'], df_year_month['Temperature (C)'], alpha=0.5, label='Data')
plt.plot(df_year_month['Formatted Date'], mymodel, color='red', label='Fitted Line')

# Set the plot title and labels
plt.title('Temperature Over Time in December 2015')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.legend()
print(r_value)
print(p_value)
# Show the plot
plt.show()
