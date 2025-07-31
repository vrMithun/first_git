import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
tables = soup.find_all("table")
tesla_table = tables[1]
table_html = str(tesla_table)

tesla_revenue = pd.read_html(table_html)[0]

# Debug: print columns to check exact names
print("Columns found:", tesla_revenue.columns)

# Clean column names by stripping whitespace/newlines
tesla_revenue.columns = tesla_revenue.columns.str.strip()

# Now rename the revenue column if needed (adjust the index if Revenue is second column)
tesla_revenue.rename(columns={tesla_revenue.columns[1]: "Revenue"}, inplace=True)

# Clean the Revenue column
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r',|\$', "", regex=True)

# Remove null or empty rows in Revenue
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

print(tesla_revenue.tail())
