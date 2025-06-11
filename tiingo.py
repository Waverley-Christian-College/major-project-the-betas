import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os


# Your Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")


# Parameter
symbol_1 = input("what's your first company you choose? ").strip().upper()
symbol_2 = input("what's your second comapany you choose? ").strip().upper()
start_date = "2025-05-01"
end_date = "2025-05-28"

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
response = requests.get(url_1, headers=headers, params=params)
data = response.json()



# Extract dates and closing prices
dates = [entry["date"][:10] for entry in data]
closes = [entry["close"] for entry in data]

# Plotting
plt.figure(figsize=(20, 5))
plt.plot(dates, closes, marker='o')
plt.title(f"{symbol_1} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("Jonathan_Test.png")
