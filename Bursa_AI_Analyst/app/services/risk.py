import numpy as np
import pandas as pd

def calculate_risk(df: pd.DataFrame) -> dict:
    """
    Calculate volatility and maximum drawdown
    """

    if df.empty or "Close" not in df.columns:
        return {
            "volatility": None,
            "max_drawdown": None
        }

    returns = df["Close"].pct_change().dropna()
    volatility = float(np.std(returns))

    max_drawdown = float(
        (df["Close"] / df["Close"].cummax() - 1).min()
    )

    return {
        "volatility": round(volatility, 4),
        "max_drawdown": round(max_drawdown, 4)
    }
