"""A page with functions to calculate financial ratios and metrics."""

import general_functions as gf
import yfinance as yf
import pandas as pd

def get_open(hist):
    return round(hist['Open'].iloc[0], 2)

def get_close(hist):
    return round(hist['Close'].iloc[-1], 2)

def get_high(hist):
    return round(hist['High'].max(), 2)

def get_low(hist):
    return round(hist['Low'].min(), 2)

def get_volume(hist):
    return round(hist['Volume'].sum() / 1_000_000, 2)

def get_total_revenue(financials, year):
    year_cols = [col for col in financials.columns if col.year == year]
    if 'Total Revenue' in financials.index and year_cols:
        return round(financials.loc['Total Revenue', year_cols].sum(), 2)
    return "N/A"

liquidity_ratios = {
    "current_ratio": "Current Ratio",
    "quick_ratio": "Quick Ratio",
    "cash_ratio": "Cash Ratio",
    "nwc_ratio": "Net Working Capital Ratio"
}

def get_current_ratio(balance_sheet, year):
    try:
        # Find all columns for the requested year
        year_cols = [col for col in balance_sheet.columns if pd.to_datetime(col).year == year]
        if not year_cols:
            return "N/A1"

        # Use correct labels from balance_sheet.index
        if "Current Assets" not in balance_sheet.index or "Current Liabilities" not in balance_sheet.index:
            return "N/A2"

        current_assets = balance_sheet.loc["Current Assets", year_cols].sum()
        current_liabilities = balance_sheet.loc["Current Liabilities", year_cols].sum()

        if current_liabilities == 0:
            return "N/A3"

        return round(current_assets / current_liabilities, 2)

    except Exception as e:
        print(f"[DEBUG] Error in get_current_ratio: {e}")
        return "N/A4"




def get_quick_ratio(financials, year):
    try:
        year_cols = [col for col in financials.columns if col.year == year]
        if not year_cols:
            return "N/A"

        current_assets = financials.loc.get("Total Current Assets", None)
        inventories = financials.loc.get("Inventory", 0)  # Inventory may be missing; default to 0
        current_liabilities = financials.loc.get("Total Current Liabilities", None)

        if current_assets is not None and current_liabilities is not None:
            total_assets = current_assets[year_cols].sum()
            total_inventory = inventories[year_cols].sum() if inventories is not None else 0
            total_liabilities = current_liabilities[year_cols].sum()

            if total_liabilities == 0:
                return "N/A"

            quick_ratio = (total_assets - total_inventory) / total_liabilities
            return round(quick_ratio, 2)
        else:
            return "N/A"
    except Exception:
        return "N/A"

def calc_cash_ratio(cash_and_cash_equivalents, current_liabilities):  #calculates cash ratio
    if current_liabilities == 0:
        return None  # change to value error if going to user
    cash_ratio = cash_and_cash_equivalents / current_liabilities
    return cash_ratio

def calc_nwc_ratio(net_working_capital, revenue): #calculates net working capital ratio
    if revenue == 0:
        return None  # change to value error if going to user
    nwc_ratio = net_working_capital / revenue
    return nwc_ratio

profitability_ratios = {
    "gross_profit_margin": "Gross Profit Margin",
    "operating_profit_margin": "Operating Profit Margin",
    "net_profit_margin": "Net Profit Margin",
    "return_on_assets": "Return on Assets",
    "return_on_equity": "Return on Equity",
    "return on investment": "Return on Investment",
    "return_on_investment_capital": "Return on Investment Capital"
}
def calc_gross_profit_margin(gross_profit, revenue):  #calculates gross profit margin
    if revenue == 0:
        return None  # change to value error if going to user
    gross_profit_margin = gross_profit / revenue
    return gross_profit_margin

def calc_operating_profit_margin(operating_profit, revenue):  #calculates operating profit margin
    if revenue == 0:
        return None  # change to value error if going to user
    operating_profit_margin = operating_profit / revenue
    return operating_profit_margin

def calc_net_profit_margin(net_profit, revenue):  #calculates net profit margin
    if revenue == 0:
        return None  # change to value error if going to user
    net_profit_margin = net_profit / revenue
    return net_profit_margin

def calc_return_on_assets(net_income, total_assets):  #calculates return on assets
    if total_assets == 0:
        return None  # change to value error if going to user
    return_on_assets = net_income / total_assets
    return return_on_assets

def return_on_equity(net_income, shareholder_equity):  #calculates return on equity
    if shareholder_equity == 0:
        return None  # change to value error if going to user
    return_on_equity = net_income / shareholder_equity
    return return_on_equity

def calc_return_on_investment(investment_gain, investment_cost):  #calculates return on investment
    if investment_cost == 0:
        return None
    return_on_investment = (investment_gain - investment_cost) / investment_cost
    return return_on_investment

def calc_return_on_investment_capital(ebit, tax_rate, invested_capital):  #calculates return on investment capital
    if invested_capital == 0:
        return None  # change to value error if going to user
    after_tax_ebit = ebit * (1 - tax_rate)
    return_on_investment_capital = after_tax_ebit / invested_capital
    return return_on_investment_capital

efficiency_ratios = {
    "asset_turnover_ratio": "Asset Turnover Ratio",
    "inventory_turnover_ratio": "Inventory Turnover Ratio",
    "receivables_turnover_ratio": "Receivables Turnover Ratio",
    "days_sales_outstanding": "Days Sales Outstanding",
    "accounts_payable_turnover_ratio": "Accounts Payable Turnover Ratio"
}

def calc_asset_turnover_ratio(revenue, total_assets):  #calculates asset turnover ratio
    if total_assets == 0:
        return None  # change to value error if going to user
    asset_turnover_ratio = revenue / total_assets
    return asset_turnover_ratio

def calc_inventory_turnover_ratio(cost_of_goods_sold, average_inventory):  #calculates inventory turnover ratio
    if average_inventory == 0:  
        return None  # change to value error if going to user
    inventory_turnover_ratio = cost_of_goods_sold / average_inventory
    return inventory_turnover_ratio

def calc_receivables_turnover_ratio(revenue, average_accounts_receivable):  #calculates receivables turnover ratio
    if average_accounts_receivable == 0:
        return None # change to value error if going to user
    receivables_turnover_ratio = revenue / average_accounts_receivable
    return receivables_turnover_ratio

def calc_days_sales_outstanding(revenue, average_accounts_receivable): #calculates days sales outsranding
    if average_accounts_receivable == 0:
        return None  # change to value error if going to user
    receivables_turnover_ratio = calc_receivables_turnover_ratio(revenue, average_accounts_receivable)
    if receivables_turnover_ratio == 0:
        return None  # change to value error if going to user
    days_sales_outstanding = 365 / receivables_turnover_ratio
    return days_sales_outstanding

def calc_accounts_payable_turnover_ratio(cost_of_goods_sold, average_accounts_payable):  #calculates accounts payable turnover ratio
    if average_accounts_payable == 0:
        return None  # change to value error if going to user
    accounts_payable_turnover_ratio = cost_of_goods_sold / average_accounts_payable
    return accounts_payable_turnover_ratio

leverage_ratios = {
    "debt_to_equity_ratio": "Debt to Equity Ratio",
    "debt_ratio": "Debt Ratio",
    "equity_ratio": "Equity Ratio",
    "interest_coverage_ratio": "Interest Coverage Ratio",
    "financial_leverage_ratio": "Financial Leverage Ratio"
}

def calc_debt_to_equity_ratio(total_liabilities, shareholder_equity):  #calculates debt to equity ratio
    if shareholder_equity == 0:
        return None  # change to value error if going to user
    debt_to_equity_ratio = total_liabilities / shareholder_equity
    return debt_to_equity_ratio

def calc_debt_ratio(total_liabilities, total_assets):  #calculates debt ratio
    if total_assets == 0:
        return None  # change to value error if going to user
    debt_ratio = total_liabilities / total_assets   
    return debt_ratio

def calc_equity_ratio(shareholder_equity, total_assets):  #calculates equity ratio
    if total_assets == 0:
        return None  # change to value error if going to user
    equity_ratio = shareholder_equity / total_assets
    return equity_ratio

def interest_coverage_ratio(ebit, interest_expense):  #calculates interest coverage ratio
    if interest_expense == 0:
        return None  # change to value error if going to user
    interest_coverage_ratio = ebit / interest_expense
    return interest_coverage_ratio

def calc_financial_leverage_ratio(total_assets, shareholder_equity):  #calculates financial leverage ratio
    if shareholder_equity == 0:
        return None  # change to value error if going to user
    financial_leverage_ratio = total_assets / shareholder_equity
    return financial_leverage_ratio

market_value_ratios = {
    "earnings_per_share": "Earnings Per Share",
    "price_to_earnings_ratio": "Price to Earnings Ratio",
    "price_to_book_ratio": "Price to Book Ratio",
    "market_capitalization": "Market Capitalization",
    "dividend_yield": "Dividend Yield",
    "dividend_payout_ratio": "Dividend Payout Ratio"
}

def calc_earnings_per_share(net_income, weighted_average_shares_outstanding):  #calculates earnings per share
    if weighted_average_shares_outstanding == 0:
        return None  # change to value error if going to user
    earnings_per_share = net_income / weighted_average_shares_outstanding
    return earnings_per_share

def calc_price_to_earnings_ratio(market_price_per_share, earnings_per_share):  #calculates price to earnings ratio
    if earnings_per_share == 0:
        return None  # change to value error if going to user
    price_to_earnings_ratio = market_price_per_share / earnings_per_share
    return price_to_earnings_ratio

def calc_price_to_book_ratio(market_price_per_share, book_value_per_share):  #calculates price to book ratio
    if book_value_per_share == 0:
        return None  # change to value error if going to user
    price_to_book_ratio = market_price_per_share / book_value_per_share
    return price_to_book_ratio

def calc_market_capitalization(market_price_per_share, weighted_average_shares_outstanding):  #calculates market capitalization
    if weighted_average_shares_outstanding == 0:
        return None  # change to value error if going to user
    market_capitalization = market_price_per_share * weighted_average_shares_outstanding
    return market_capitalization

def calc_dividend_yield(dividend_per_share, market_price_per_share):  #calculates dividend yield
    if market_price_per_share == 0:
        return None  # change to value error if going to user
    dividend_yield = dividend_per_share / market_price_per_share
    return dividend_yield

def calc_dividend_payout_ratio(dividend_per_share, earnings_per_share):  #calculates dividend payout ratio
    if earnings_per_share == 0:
        return None  # change to value error if going to user
    dividend_payout_ratio = dividend_per_share / earnings_per_share
    return dividend_payout_ratio

def calc_custom():
    # Placeholder for custom ratio calculation logic
    return "Custom ratio calculation not implemented yet."

