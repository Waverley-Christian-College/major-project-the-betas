[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9x6qoLrK)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19374581)
# 📈 Stock Price Plotter

This project teaches you how to use a real-world API (Tiingo) to:
- Fetch stock market data
- Parse JSON responses
- Plot closing prices using matplotlib

## 🚀 Instructions

1. Open this repo in GitHub Codespaces or VS Code.
2. Run the following to install required packages:
   ```bash
   pip install -r requirements.txt
3. Use the API token provided for you in MS TEAMS
4. Replace `"your_tiingo_api_token"` in `tiingo_stock_plot.py` with your actual token.
5. Run the script: `python tiingo_stock_plot.py`

# 📈 Stock Volatility Tracker


## 🎯 Purpose

The **Stock Volatility Tracker** is a finance tool that identifies when the market experiences significant price fluctuations (volatility), either up or down. This is an important component in risk assessment when investing in stocks. Our tool leverages data from the Tiingo API to visualize periods of unusual price movements through intuitive graphs, tables, and actionable insights.


## ✨ Features

### 📊 Volatility Visualization
Interactive charts displaying historical volatility allow users to see historical fluctuations at a glance. These visualizations help investors identify periods of high and low volatility, providing crucial context for making informed purchase decisions.

### 🔮 Volatility Prediction
Our tracker employs statistical models such as GARCH (Generalized Autoregressive Conditional Heteroskedasticity), a sophisticated algorithm that helps predict future volatility trends, making it easier to develop investment strategies with confidence.

### ⏱️ Customizable Timeframes
Users can select specific timeframes (e.g., 1 month, 3 months, or 1 year) for analysis. This flexibility supports comprehensive trend analysis and empowers investors when making crucial financial decisions.

## 📋 How It Works

1. **Data Retrieval**: Connect to Tiingo API to fetch historical stock price data
2. **Analytics Processing**: Calculate volatility metrics across different time periods
3. **Pattern Recognition**: Identify periods of unusually high or low volatility
4. **Visualization**: Generate interactive charts and tables for intuitive understanding


## 👨‍💻 Contributors

- **David Ibrahim** - *Visualization & User Interface*
- **Jonathan McNaught** - *Data Retrieval & Core Metrics*
- **Ethan Gunadi** - *Analysis & Advanced Metrics*

*Made with ❤️ for Year 9 Computer Science Project*

