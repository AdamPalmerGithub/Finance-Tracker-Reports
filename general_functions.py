"""A file containing general functions for the finance tracker and reporting app."""

import ratio_functions as rf
import yfinance as yf


def set_ticker(ticker: str):
    return yf.Ticker(ticker.upper())



