# 📊 Stock Comparison Tool

## 🎯 Purpose
The **Stock Comparison Tool** is a finance application that allows investors to compare the performance of two different stocks side-by-side. By visualizing both stocks on the same graph with dual trend lines, users can easily identify which stock has performed better over specific time periods. This tool leverages data from the Tiingo API to provide accurate historical price data and meaningful comparative analysis for informed investment decisions.

## ✨ Features

### 📈 Side-by-Side Visualization
Interactive dual-line charts that display two stocks simultaneously, making it easy to compare price movements, trends, and performance patterns at a glance. Each stock is represented by a distinct colored line for clear differentiation.

### 🔍 Brief Analysis of Stocks
Starting and Closing prices of the user selected stocks are displayed alongside the percentage change.

### ⏱️ Flexible Time Periods
Users can select custom timeframes (1 month, 3 months, 6 months, 1 year or custom) for comparison analysis. This flexibility enables both short-term trading insights and long-term investment strategy development.


## 📋 How It Works

1. **Stock Selection**: Choose two different stocks using their ticker symbols (e.g., AAPL vs GOOGL)
2. **Data Retrieval**: Connect to Tiingo API to fetch historical price data for both stocks
3. **Data Processing**: Normalize and align the data for accurate comparison
4. **Visualization**: Generate dual-line interactive charts showing both stocks' performance
5. **Analysis**: Calculate comparative metrics and performance statistics

## 🚀 Getting Started

### Step-by-Step Installation (Simple Instructions)

**Before you begin:**
- Make sure you have Python installed on your computer
- You'll need a free API key from [Tiingo](https://www.tiingo.com/) (sign up for free)

**Step 1: Get the code**
```bash
# Download the project from GitHub
git clone https://github.com/Waverley-Christian-College/major-project-the-betas
```

**Step 2: Open the project**
```bash
# Go into the project folder
cd stock-comparison-tool
```

**Step 3: Install required packages**
```bash
# Install all the Python packages we need
pip install -r requirements.txt
```

**Step 4: Add your API key**
Create a new file called `.env` in the project folder and add:
```
TIINGO_API_KEY=your_actual_api_key_here
```
*(Replace "your_actual_api_key_here" with the real API key you got from Tiingo)*

**Step 5: Run the program**
```bash
# Start the stock comparison tool
python main.py
```

**That's it!** The program should now open and you can start comparing stocks by entering their ticker symbols (like AAPL for Apple or GOOGL for Google).

## 👨‍💻 Contributors
* **David Ibrahim** 
* **Jonathan McNaught** 
* **Ethan Gunadi** 

*Made with ❤️ for Year 9 Computer Science Project*