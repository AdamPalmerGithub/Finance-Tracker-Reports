import yfinance as yf
import pandas as pd

ticker = yf.Ticker("AAPL")

# Print Financials Info
financials = ticker.financials
balance_sheet = ticker.balance_sheet

print("=== FINANCIALS ===")
print(financials)

print("=== BALANCE SHEET ===")
print(balance_sheet)

# Optional: Show current assets & liabilities
print("Current Assets label exists:", "Current Assets" in balance_sheet.index)
print("Current Liabilities label exists:", "Current Liabilities" in balance_sheet.index)

# Get historical price data for 2024
history_2024 = ticker.history(start="2024-01-01", end="2025-01-01")

# Calculate and print average closing price for 2024
average_close_2024 = history_2024["Close"].mean()
print("=== AVERAGE CLOSING PRICE FOR AAPL IN 2024 ===")
print(f"${average_close_2024:.2f}")