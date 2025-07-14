import streamlit as st
import pandas as pd 
import yfinance as yf
from general_functions import set_ticker, get_yearly_data
from ratio_functions import *
from listed_items import years, sorted_metrics

st.title('📊 Ratio Calculator' )

ticker_input = st.text_input("🔍 Enter a stock ticker", placeholder="e.g. AAPL")

# Multiselect box for selecting multiple years
selected_years = st.multiselect(
    'Select the years you want to display:',
    options=years,
    default=[2025]
)

selected_metrics = st.multiselect(
    'Select the metrics you want to display:',
    options=sorted_metrics,
    default = ["Open", "Close"]
)

ordered_selected_years = [y for y in years if y in selected_years] #sorted selected years

if ticker_input:
    try:
        track = set_ticker(ticker_input) #Takes user input and sets ticker
        info = track.info  # May raise an error if ticker is invalid

        st.subheader(f"{info.get('shortName', 'Unknown Company')} ({ticker_input.upper()})")
        st.write(f"Current Price: ${info.get('regularMarketPrice', 'N/A')}")
        st.write("Sector:", info.get("sector", "N/A"))
        st.write("Market Cap:", info.get("marketCap", "N/A"))



        if ordered_selected_years:
            st.markdown("### Selected Years:")
            cols = st.columns(len(ordered_selected_years))
            
            for i, year in enumerate(ordered_selected_years):
                with cols[i]:
                    yearly_data = get_yearly_data(track, year, selected_metrics)

                    st.markdown(f"**{year}**")
                    if isinstance(yearly_data, dict):
                        for metric in selected_metrics:
                            value = yearly_data.get(metric, "N/A")
                            st.metric(label=metric, value=value)
                    else:
                        st.error(yearly_data)         

    except Exception as e:
        st.error(f"Could not retrieve data for '{ticker_input}'. Error: {e}")



# Get and display balance sheet
try:
    stock = yf.Ticker(ticker_input)
    balance_sheet = stock.balance_sheet

    st.subheader("📄 Balance Sheet")
    if balance_sheet.empty:
        st.error("⚠️ No balance sheet data found for this ticker.")
    else:
        st.dataframe(balance_sheet)
        st.success("✅ Balance sheet data fetched successfully!")

except Exception as e:
    st.error(f"⚠️ Could not fetch balance sheet data. Error: {e}")


 # Get and Display Profit Loss

st.subheader("📄 Profit and Loss Statement")
pnl = stock.financials

if not pnl.empty:
    st.dataframe(pnl)
    st.success("✅ Profit & Loss data fetched successfully!")
else:
    st.error("⚠️ No P&L data found for this ticker.")





# st.write('Upload your files to get started')

# # Upload Files
# balance_sheet = st.file_uploader("Upload your balance sheet (CSV or Excel)", type=["csv", "xlsx"])
# profit_loss = st.file_uploader ('Upload your profit and loss statement (CSV or Excel)')

# # Show results if both are uploaded
# if balance_sheet is not None and profit_loss is not None:
#     st.success('✅ Files uploaded!')
    
# st.subheader("📄 Balance Sheet Preview")
# st.dataframe(balance_sheet)

# st.subheader("📄 Profit & Loss Statement Preview")
# st.dataframe(profit_loss)

# st.subheader("📊 Calculated Ratios")


# col1, col2 = st.columns(2)

# with col1:
#         st.metric("Current Ratio", "—")
#         st.metric("Debt to Equity Ratio", "—")
#         st.metric("Asset Turnover Ratio", "—")
#         st.metric("Inventory Turnover Ratio", "—")
#         st.metric("Debt Ratio", "—")

# with col2:
#         st.metric("Debtors Turnover Ratio", "—")
#         st.metric("Gross Profit Ratio", "—")
#         st.metric("Interest Coverage Ratio", "—")
#         st.metric("Profitability Ratio", "—")
#         st.metric("Quick Ratio", "—")
#         st.metric("Return on Assets", "—")

