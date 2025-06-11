import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os
import os

# Your Tiingo API token
#API_TOKEN = os.getenv("API_TOKEN")
API_TOKEN = "d0r5o7hr01qn4tjgl0hgd0r5o7hr01qn4tjgl0i0"
print(f"This is my {API_TOKEN}")


# Parameter
symbol_1 = "NVDA"
symbol_2 = "AAPL"
start_date = "2025-04-01"
end_date = "2025-05-01"

url = f"https://api.tiingo.com/tiingo/daily/{symbol_1}/prices"
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
response = requests.get(url, headers=headers, params=params)
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

plt.figure(figsize=(20, 5))
plt.plot(dates, closes, marker='o')
plt.title(f"{symbol_2} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("david_test2.png")
