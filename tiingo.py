# ===== IMPORT REQUIRED LIBRARIES =====
# These are the external libraries we need for our stock comparison tool
import requests          # Used to make HTTP requests to the Tiingo API
import json             # Used to handle JSON data (though not directly used in this code)
from datetime import datetime, timedelta  # Used for date calculations and formatting
import matplotlib.pyplot as plt           # Used to create graphs and charts
import os               # Used to access environment variables (like API keys)

# ===== API SETUP AND CONFIGURATION =====
# Get the API token from environment variables for security
# This keeps our API key private and not visible in the code
API_TOKEN = os.getenv("API_TOKEN")

# Check if the API token exists, if not, warn the user
if not API_TOKEN:
    print("⚠️  Warning: API_TOKEN environment variable not found!")
    print("   Please set your Tiingo API token as an environment variable.")

# ===== DISPLAY WELCOME MESSAGE =====
# Create a nice header with decorative lines to make the tool look professional
print("=" * 60)                          # Print 60 equal signs for a border
print("📈 STOCK COMPARISON TOOL 📈")      # Main title with emoji
print("=" * 60)                          # Another border line
print("Compare the performance of two stocks over time!")  # Description
print("-" * 60)                          # Dashed line separator

# ===== GET STOCK SYMBOLS FROM USER =====
# Ask the user to input two company stock symbols (like AAPL, GOOGL, etc.)
symbol_1 = input("What's your first company you choose? ").strip().upper()
# .strip() removes any extra spaces, .upper() converts to uppercase

symbol_2 = input("What's your second comapany you choose? ").strip().upper()
# Same process for the second stock symbol

# Confirm the selected stocks to the user with a checkmark emoji
print(f"\n✅ Selected stocks: {symbol_1} vs {symbol_2}")

# ===== DISPLAY TIME PERIOD OPTIONS =====
# Show the user different time period options they can choose from
print("\n📅 TIME PERIOD SELECTION:")      # Section header with calendar emoji
print("\nChoose your time period:")       # Instruction text
print("1. Last 1 month")                  # Option 1
print("2. Last 3 months")                 # Option 2
print("3. Last 6 months")                 # Option 3
print("4. Last 1 year")                   # Option 4
print("5. Custom dates")                  # Option 5 - user can enter their own dates
print("-" * 30)                           # Separator line

# Get the user's choice for time period
timechoice = input("Enter your time period selection (1-5): ").strip()

# ===== DATE SETUP =====
# Get today's date to use as a reference point for calculations
today = datetime.now()  # Gets current date and time
dateformat = "%Y-%m-%d"  # Define date format as YYYY-MM-DD (e.g., 2024-01-15)

# ===== CALCULATE DATE RANGES BASED ON USER CHOICE =====
# Use if-elif-else statements to handle different time period options
if timechoice == "1":  # User chose 1 month
    # Handle special case: if current month is January, go back to December of previous year
    if today.month == 1:
        start_date = today.replace(year = today.year - 1, month = 12).strftime(dateformat)
    else:
        # For other months, just subtract 1 from current month
        start_date = today.replace(month = today.month - 1).strftime(dateformat)
    
    # End date is always today
    end_date = today.strftime(dateformat)
    
elif timechoice == "2":  # User chose 3 months
    # Calculate 3 months back from current date
    new_month = today.month - 3
    new_year = today.year
    
    # Handle year crossing (e.g., if current month is February, 3 months back is November of previous year)
    if new_month <= 0:  # If month becomes 0 or negative
        new_month += 12  # Add 12 to get correct month
        new_year -= 1    # Subtract 1 from year
    start_date = today.replace(year=new_year, month=new_month).strftime(dateformat)
      
    end_date = today.strftime(dateformat)

elif timechoice == "3":  # User chose 6 months
    # Calculate 6 months back from current date
    new_month = today.month - 6
    new_year = today.year
    
    # Handle year crossing (same logic as 3 months but with 6)
    if new_month <= 0: 
        new_month += 12
        new_year -= 1
    start_date = today.replace(year=new_year, month=new_month).strftime(dateformat)
      
    end_date = today.strftime(dateformat)

elif timechoice == "4":  # User chose 1 year
    # Simply subtract 1 year from current date
    start_date = today.replace(year = today.year - 1).strftime(dateformat)
    end_date = today.strftime(dateformat)

elif timechoice == "5":  # User chose custom dates
    # Let user enter their own start and end dates
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate the dates the user entered
    try:
        # Try to parse the dates to make sure they're in correct format
        startdt = datetime.strptime(start_date, "%Y-%m-%d")
        enddt = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Check if start date is before end date (logical requirement)
        if startdt >= enddt:
            print("❌Error: Start date must be before end date.")
            exit()  # Stop the program if dates are invalid

    except ValueError:  # If date parsing fails
        print("❌Error: Invalid date format. Please use YYYY-MM-DD.")
        exit()  # Stop the program if format is wrong

else:  # User entered invalid choice (not 1-5)
    # Default to 1 month if user enters invalid option
    print("⚠️Invalid time choice. Using 1 month as a default.")
    if today.month == 1:
        start_date = today.replace(year = today.year - 1, month = 12).strftime(dateformat)
    else:
        start_date = today.replace(month = today.month - 1).strftime(dateformat)
        end_date = today.strftime(dateformat)

# Display the final date range to the user
print(f"📅 Comparing stocks from {start_date} to {end_date}")
print("-" * 60)  # Separator line

# ===== PREPARE API REQUESTS =====
# Build the URLs for the Tiingo API endpoints for both stocks
url_1 = f"https://api.tiingo.com/tiingo/daily/{symbol_1}/prices"
url_2 = f"https://api.tiingo.com/tiingo/daily/{symbol_2}/prices"

# Set up headers for the API request (required by Tiingo)
headers = {
    "Content-Type": "application/json",        # Tell API we want JSON response
    "Authorization": f"Token {API_TOKEN}"      # Include our API token for authentication
}

# Set up parameters for the API request
params = {
    "startDate": start_date,      # When to start getting data
    "endDate": end_date,          # When to stop getting data
    "resampleFreq": "daily"       # Get daily price data (not hourly/weekly)
}

# ===== FETCH DATA FROM API =====
# Make HTTP requests to get stock data from Tiingo API
print(f"🔄Fetching data for {symbol_1}...")  # Status message for user
response_1 = requests.get(url_1, headers=headers, params=params)  # Make the request
data_1 = response_1.json()  # Convert response to JSON format

print(f"🔄Fetching data for {symbol_2}...")  # Status message for second stock
response_2 = requests.get(url_2, headers=headers, params=params)  # Make the request
data_2 = response_2.json()  # Convert response to JSON format

# ===== ERROR CHECKING =====
# Check if the API returned any errors (like invalid stock symbols)
if ("detail" in str(data_1)) or ("detail" in str(data_2)): 
    # If "detail" appears in response, it usually means an error occurred
    print("❌Error: Could not retrieve data for one or both stocks or Invalid stock Symbol")
    exit()  # Stop the program if there's an error

# ===== EXTRACT PRICE DATA =====
# Extract the dates and closing prices from the JSON data
# Each entry in the data contains: date, open, high, low, close, volume
dates_1 = [entry["date"][:10] for entry in data_1]  # Get first 10 characters of date (YYYY-MM-DD)
closes_1 = [entry["close"] for entry in data_1]     # Get closing price for each day

dates_2 = [entry["date"][:10] for entry in data_2]  # Same for second stock
closes_2 = [entry["close"] for entry in data_2]

# ===== DISPLAY COMPARISON SUMMARY =====
# Create a nice summary section showing key statistics
print("\n" + "=" * 60)      # New line plus border
print("📊 COMPARISON SUMMARY")  # Section title with chart emoji
print("=" * 60)             # Border line

# Calculate start and end prices for both stocks
start_price_1 = closes_1[0]   # First price in the list (oldest date)
end_price_1 = closes_1[-1]    # Last price in the list (newest date, -1 means last item)

start_price_2 = closes_2[0]   # Same for second stock
end_price_2 = closes_2[-1]

# Calculate percentage change for both stocks
# Formula: ((end_price - start_price) / start_price) * 100
change_1 = ((end_price_1 - start_price_1) / start_price_1) * 100
change_2 = ((end_price_2 - start_price_2) / start_price_2) * 100

# Display statistics for first stock
print(f"{symbol_1}:")
print(f"  Start Price: ${start_price_1:.2f}")  # :.2f formats to 2 decimal places
print(f"  End Price:   ${end_price_1:.2f}")
print(f"  Change:      {change_1:+.2f}%")      # :+.2f shows + or - sign with 2 decimals

# Display statistics for second stock
print(f"\n{symbol_2}:")  # \n adds a blank line
print(f"  Start Price: ${start_price_2:.2f}")
print(f"  End Price:   ${end_price_2:.2f}")
print(f"  Change:      {change_2:+.2f}%")

# ===== COMPARE FINAL PRICES =====
# Compare which stock ended at a higher price
if closes_1[-1] > closes_2[-1]:  # If first stock's final price is higher
    print(f"🟢 {symbol_1} ended higher than {symbol_2}")

elif closes_2[-1] > closes_1[-1]:  # If second stock's final price is higher
    print(f"🟢 {symbol_2} ended higher than {symbol_1}")

else:  # If both stocks ended at exactly the same price (rare)
    print("📊 Both stocks ended at the same price")

# Tell user to look at the graph
print("Please refer to the graph to compare the 2 stocks!")

# Display completion message
print("=" * 60)
print("✨ Analysis complete! Thank you for using the Stock Comparison Tool!")
print("=" * 60)

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

plt.savefig(f"{symbol_1} VS {symbol_2}.png")  # Save the plot
plt.show()
