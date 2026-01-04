import pandas as pd

def calculate_indicators(df: pd.DataFrame):
    close_price = float(df["Close"].iloc[-1])

    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    sma_20 = df["Close"].rolling(20).mean().iloc[-1]

    return {
        "close_price": round(close_price, 2),
        "rsi": round(float(rsi.iloc[-1]), 2),
        "sma_20": round(float(sma_20), 2)
    }
