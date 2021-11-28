import streamlit as st 
import pandas as pd
import yahoo_fin.stock_info as yf 
import numpy as np

# DATA
stocks_earnings_dates = [
    str(yf.get_next_earnings_date('MELI').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('AAPL').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('KO').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('TSLA').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('AMZN').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('MSFT').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('INTC').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('GOLD').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('XOM').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('NFLX').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('BAC').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('JPM').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('DIS').strftime("%d-%b-%Y")),
    str(yf.get_next_earnings_date('FB').strftime("%d-%b-%Y")),] 
stocks_symbols = np.array([
    "MELI",
    "AAPL",
    "KO",
    "TSLA",
    "AMZN",
    "MSFT",
    "INTC",
    "GOLD",
    "XOM",
    "NFLX",
    "BAC",
    "JPM",
    "DIS",
    "FB",])

df = pd.DataFrame(stocks_earnings_dates, stocks_symbols)

# Site
st.title("CEDEAR's Calendar")
st.subheader("Earnings calendar")
dfstream = st.table(df)

st.markdown("By: Domingo Montoya", unsafe_allow_html=False)


