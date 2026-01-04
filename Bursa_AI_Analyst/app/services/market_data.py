import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    try:
        df = yf.download(ticker, period=period, progress=False)
        if df.empty:
            return pd.DataFrame()
        return df
    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()
