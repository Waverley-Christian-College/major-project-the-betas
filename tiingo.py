import requests
import matplotlib.pyplot as plt

API_TOKEN = "5296eb9cb95697ef016ac7de004f18c24ecfad7c"

symbol_1 = "NVDA"
symbol_2 = "AAPL"
start_date = "2025-04-01"
end_date = "2025-05-01"

def fetch_stock_data(symbol):
    url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}"
    }
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "resampleFreq": "daily"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return [], []

    data = response.json()

    dates = [entry["date"][:10] for entry in data]
    closes = [entry["close"] for entry in data]

    return dates, closes

# Fetch data
dates_1, closes_1 = fetch_stock_data(symbol_1)
dates_2, closes_2 = fetch_stock_data(symbol_2)

# Plotting
plt.figure(figsize=(20, 5))
plt.plot(dates_1, closes_1, marker='o', label=symbol_1)
plt.plot(dates_2, closes_2, marker='o', label=symbol_2)

plt.title(f"{symbol_1} & {symbol_2} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()  # legend

plt.savefig("david_test5.png")  # Save the plot
plt.show()
