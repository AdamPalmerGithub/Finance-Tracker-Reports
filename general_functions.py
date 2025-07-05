"""A file containing general functions for the finance tracker and reporting app."""

import ratio_functions as rf
import yfinance as yf


def set_ticker(ticker: str):
    return yf.Ticker(ticker.upper())

def get_yearly_data(ticker_obj, year):

    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    try:
        hist = ticker_obj.history(start=start_date, end=end_date)
        if hist.empty:
            return "No data available"
        
        # Optionally: calculate yearly stats/ratios
        return {
            "Open": round(hist['Open'].iloc[0], 2),
            "Close": round(hist['Close'].iloc[-1], 2),
            "High": round(hist['High'].max(), 2),
            "Low": round(hist['Low'].min(), 2),
            "Volume (M)": round(hist['Volume'].sum() / 1_000_000, 2),
        }
    except Exception as e:
        return f"Error: {e}"


