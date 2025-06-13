import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os


# Your Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")


# Parameter
symbol_1 = input("What's your first company you choose? ").strip().upper() 
symbol_2 = input("What's your second comapany you choose? ").strip().upper()

# Time Periods
print("\nChoose your time period:")
print("1. Last 1 month")
print("2. Last 3 months") 
print("3. Last 6 months")
print("4. Last 1 year")
print("5. Custom dates")

timechoice = input("Enter your time period selection (1-5): ").strip()

today = datetime.now() #got lazy of writing that thing a lot
dateformat = "%Y-%m-%d"

#Time Choices (basically does some time math)
if timechoice == "1":
    if today.month == 1:
        start_date = today.replace(year = today.year - 1, month = 12).strftime(dateformat)
    else:
        start_date = today.replace(month = today.month - 1).strftime(dateformat)
    
    end_date = today.strftime(dateformat)
    
elif timechoice == "2":
    new_month = today.month - 3
    new_year = today.year
    
    if new_month <= 0:  # Handle year crossing
        new_month += 12
        new_year -= 1
    start_date = today.replace(year=new_year, month=new_month).strftime(dateformat)
      
    end_date = today.strftime(dateformat)

elif timechoice == "3":
    new_month = today.month - 6
    new_year = today.year
    
    if new_month <= 0: 
        new_month += 12
        new_year -= 1
    start_date = today.replace(year=new_year, month=new_month).strftime(dateformat)
      
    end_date = today.strftime(dateformat)

elif timechoice == "4":
    start_date = today.replace(year = today.year - 1).strftime(dateformat)

    end_date = today.strftime(dateformat)
#error message:
elif timechoice == "5":
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        startdt = datetime.strptime(start_date, "%Y-%m-%d")
        enddt = datetime.strptime(end_date, "%Y-%m-%d")
        
        if startdt >= enddt:
            print("Error: Start date must be before end date.")
            exit()

    except ValueError: 
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        exit()

else:
    print("Invalid time choice. Using 1 month as a default.")
    if today.month == 1:
        start_date = today.replace(year = today.year - 1, month = 12).strftime(dateformat)
    else:
        start_date = today.replace(month = today.month - 1).strftime(dateformat)

        end_date = today.strftime(dateformat)

print(f"Comparing stocks from {start_date} to {end_date}")

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

#Error message
if ("detail" in str(data_1)) or ("detail" in str(data_2)): 
    print("Error: Could not retrieve data for one or both stocks or Invalid stock Symbol")
    exit()

# Extract dates and closing prices
dates_1 = [entry["date"][:10] for entry in data_1]
closes_1 = [entry["close"] for entry in data_1]

dates_2 = [entry["date"][:10] for entry in data_2]
closes_2 = [entry["close"] for entry in data_2]

start_price_1 = closes_1[0]
end_price_1 = closes_1[-1]

start_price_2 = closes_1[0]
end_price_2 = closes_1[-1]

change_1 = ((end_price_1 - start_price_1) / start_price_1) * 100
change_2 = ((end_price_2 - start_price_2) / start_price_2) * 100

print(f"{symbol_1}:")
print(f"  Start Price: ${start_price_1:.2f}")
print(f"  End Price:   ${end_price_1:.2f}")
print(f"  Change:      {change_1:+.2f}%")

print(f"\n{symbol_2}:")
print(f"  Start Price: ${start_price_2:.2f}")
print(f"  End Price:   ${end_price_2:.2f}")
print(f"  Change:      {change_2:+.2f}%")

if closes_1[-1] > closes_2[-1]:
    print(f"🟢 {symbol_1} ended higher than {symbol_2}")

elif closes_2[-1] > closes_1[-1]:
    print(f"🟢 {symbol_2} ended higher than {symbol_1}")

else:
    print("📊 Both stocks ended at the same price")

print("Please refer to the graph to compare the 2 stocks!")

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
