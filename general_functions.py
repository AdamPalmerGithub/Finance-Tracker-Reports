"""A file containing general functions for the finance tracker and reporting app."""

from ratio_functions import *
import yfinance as yf
from listed_items import *


def set_ticker(ticker: str):
    return yf.Ticker(ticker.upper())

def get_yearly_data(ticker_obj, year, selected_metrics):

    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    try:
        hist = ticker_obj.history(start=start_date, end=end_date)
        financials = ticker_obj.financials

        if hist.empty:
            return "No data available"
        
        results = {}
        if "Open" in selected_metrics:
            results["Open"] = get_open(hist)
        if "Close" in selected_metrics:
            results["Close"] = get_close(hist)
        if "High" in selected_metrics:
            results["High"] = get_high(hist)
        if "Low" in selected_metrics:
            results["Low"] = get_low(hist)
        if "Volume (M)" in selected_metrics:
            results["Volume (M)"] = get_volume(hist)
        if "Total Revenue" in selected_metrics:
            results["Total Revenue"] = get_total_revenue(financials, year)
        if "Current Ratio" in selected_metrics:
            results["Current Ratio"] = get_current_ratio(financials, year)
        if "Quick Ratio" in selected_metrics:
            results["Quick Ratio"] = get_quick_ratio(financials, year)

        return results

    except Exception as e:
        return f"Error: {e}"

