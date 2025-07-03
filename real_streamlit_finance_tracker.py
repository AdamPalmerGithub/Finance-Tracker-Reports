import streamlit as st
import pandas as pd 
import yfinance as yf

st.title('📊 Ratio Calculator' )

ticker = st.text_input("🔍 Enter a stock ticker", placeholder="e.g. AAPL")

if ticker:
    try:
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        st.subheader("📄 Balance Sheet")
        st.dataframe(balance_sheet)
        if balance_sheet.empty:
             st.error("⚠️ No balance sheet data found for this ticker.")
        else:
                st.success("✅ Balance sheet data fetched successfully!")
    except:
        st.error("⚠️ Could not fetch data. Check the ticker symbol.")




st.write('Upload your files to get started')

# Upload Files
balance_sheet = st.file_uploader("Upload your balance sheet (CSV or Excel)", type=["csv", "xlsx"])
profit_loss = st.file_uploader ('Upload your profit and loss statement (CSV or Excel)')

# Show results if both are uploaded
if balance_sheet is not None and profit_loss is not None:
    st.success('✅ Files uploaded!')
    
st.subheader("📄 Balance Sheet Preview")
st.dataframe(balance_sheet)

st.subheader("📄 Profit & Loss Statement Preview")
st.dataframe(profit_loss)

st.subheader("📊 Calculated Ratios")


col1, col2 = st.columns(2)

with col1:
        st.metric("Current Ratio", "—")
        st.metric("Debt to Equity Ratio", "—")
        st.metric("Asset Turnover Ratio", "—")
        st.metric("Inventory Turnover Ratio", "—")
        st.metric("Debt Ratio", "—")

with col2:
        st.metric("Debtors Turnover Ratio", "—")
        st.metric("Gross Profit Ratio", "—")
        st.metric("Interest Coverage Ratio", "—")
        st.metric("Profitability Ratio", "—")
        st.metric("Quick Ratio", "—")
        st.metric("Return on Assets", "—")








# Ratio that will be calculated:
# Current ratio
# Debt to equity ratio
# Asset turnover ratio
# Inventory turnover ratio
# Debt ratio
# Debtors turnover ratio
# Gross profit ratio
# Interest coverage ratio
# Profitability ratio
# Quick ratio
# Return on assets ratio