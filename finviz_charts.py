import streamlit as st
import pandas as pd

def display_finviz_charts(tickers):
    """Displays Finviz charts for the given tickers with a maximum of 3 charts per row.

    Args:
        tickers (list): A list of stock ticker symbols (e.g., ["TSLA", "AMZN", "GOOG"]).
    """
    st.header("Finviz Charts")
    num_tickers = len(tickers)
    max_cols = 3  # Maximum number of charts per row

    for i in range(0, num_tickers, max_cols):
        cols = st.columns(min(max_cols, num_tickers - i))  # Create columns for each chart in the row
        for j, ticker in enumerate(tickers[i:i + max_cols]):
            finviz_url = f"https://finviz.com/chart.ashx?t={ticker}&ty=c&ta=st_1,ta_4&p=d&s=l"  # Create finviz url
            with cols[j]:  # Place image in the respective column
                st.markdown(f'<div style="text-align:center"><a href="{finviz_url}" target="_blank"><img src="{finviz_url}" style="width: 100%; border: 2px solid #cccccc; border-radius: 5px;"/></a></div>', unsafe_allow_html=True)
                st.markdown(f'<p style="text-align:center"><a href="{finviz_url}" target="_blank">{ticker}</a></p>', unsafe_allow_html=True)  # Place name of ticker below

if __name__ == "__main__":
    tickers = ["GOOG", "AMZN", "AAPL","WMT","T","NVDA", "MSFT", "PLTR", "TSLA"]  # Example list of tickers
    display_finviz_charts(tickers)