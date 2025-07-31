import yfinance as yf
import pandas as pd
import json
import urllib.request
amd = yf.Ticker("AMD")

with open('amd.json') as json_file:
    amd_info = json.load(json_file)

print(amd_info['country'])
print(amd_info['sector'])
amd_history = amd.history(period="max")

first_day_volume = amd_history.iloc[0]['Volume']
print("Volume on first day:", first_day_volume)

'''
import urllib.request

# Download the JSON file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
urllib.request.urlretrieve(url, "amd.json")
'''