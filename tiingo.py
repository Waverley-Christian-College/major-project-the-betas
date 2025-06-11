import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os


# Your Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")


# Parameter
symbol_1 = input("what's your first company you choose? ").strip().upper() 
symbol_2 = input("what's your second comapany you choose? ").strip().upper()

# Time Periods
print("\nChoose your time period:")
print("1. Last 1 month")
print("2. Last 3 months") 
print("3. Last 6 months")
print("4. Last 1 year")
print("5. Custom dates")

timechoice = input("Enter your time period selection (1-5): ")

url_1 = f"https://api.tiingo.com/tiingo/daily/{symbol_1}/prices"
url_2 = f"https://api.tiingo.com/tiingo/daily/{symbol_2}/prices"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date,
    "endDate": end_date,
    "resampleFreq": "daily"
}

# Make the request
print(f"Fetching data for {symbol_1}...") #Status message
response_1 = requests.get(url_1, headers=headers, params=params)
data_1 = response_1.json()

print(f"Fetching data for {symbol_2}...")
response_2 = requests.get(url_2, headers=headers, params=params)
data_2 = response_2.json()

if not data_1 or not data_2: #error message
    print("Error: Could not retrieve data for one or both stocks.")
    exit()


# Extract dates and closing prices
dates_1 = [entry["date"][:10] for entry in data_1]
closes_1 = [entry["close"] for entry in data_1]

dates_2 = [entry["date"][:10] for entry in data_1]
closes_2 = [entry["close"] for entry in data_1]

# Plotting
plt.figure(figsize=(20, 5))
plt.plot(dates_1, closes_1, marker='o')
plt.title(f"{symbol_1} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("Jonathan_Test.png")
