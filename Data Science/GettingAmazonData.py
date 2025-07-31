import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Download the HTML content from the URL
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
response = requests.get(url)
html_data = response.text  # Store HTML content as string

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Step 3: Create an empty DataFrame with the required columns
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

# Step 4: Find the table body and loop through each row (tr)
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    if len(col) < 7:
        continue  # Skip rows that don't have enough columns (like empty rows)
    # Extract values from each column
    date = col[0].text.strip()
    Open = col[1].text.strip()
    high = col[2].text.strip()
    low = col[3].text.strip()
    close = col[4].text.strip()
    adj_close = col[5].text.strip()
    volume = col[6].text.strip()

    # Append to the DataFrame
    amazon_data = pd.concat([amazon_data, pd.DataFrame({
        "Date": [date],
        "Open": [Open],
        "High": [high],
        "Low": [low],
        "Close": [close],
        "Adj Close": [adj_close],
        "Volume": [volume]
    })], ignore_index=True)

# Step 5: Show the first 5 rows of the data
print(amazon_data.head())

# Step 6: Answer the exercise questions
print("\nColumn names in the DataFrame:")
print(amazon_data.columns.tolist())

print("\nOpen value of the last row:")
print(amazon_data.iloc[-1]["Open"])
