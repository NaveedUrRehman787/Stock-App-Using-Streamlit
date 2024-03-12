import streamlit as st
import yfinance as yf
import pandas as pd

# List of ticker symbols
ticker_symbols = ['GOOGL', 'AAPL', 'MSFT', 'AMZN']

st.write("""# Simple Stock Price App""")

# Use selectbox for selection of ticker
tickerSymbol = st.selectbox('Select a ticker symbol', ticker_symbols)

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2013-5-31', end='2024-2-29')

st.write(f"## Closing Price for {tickerSymbol}")
st.line_chart(tickerDF.Close)

st.write(f"## Volume Price for {tickerSymbol}")
st.line_chart(tickerDF.Volume)