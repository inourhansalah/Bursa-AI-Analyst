from fastapi import APIRouter, HTTPException
from app.services.market_data import get_stock_data
from app.services.indicators import calculate_indicators
from app.services.risk import calculate_risk
from app.crew.crew import run_crew
import math

router = APIRouter()

def safe_value(v):
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
        return None
    return v

def safe_list(values):
    return [
        None if (isinstance(v, float) and (math.isnan(v) or math.isinf(v)))
        else v
        for v in values
    ]

@router.post("/analyze-stock")
def analyze_stock(ticker: str, period: str = "1y"):
    df = get_stock_data(ticker, period)

    if df.empty:
        raise HTTPException(status_code=400, detail="No market data found")

    # Yahoo Finance fix
    close_series = df["Close"].iloc[:, 0]

    indicators = calculate_indicators(df)
    risk = calculate_risk(df)

    summary = {
        "ticker": ticker,
        "close_price": safe_value(indicators["close_price"]),
        "rsi": safe_value(indicators["rsi"]),
        "sma_20": safe_value(indicators["sma_20"]),
        "risk": {
            "volatility": safe_value(risk["volatility"]),
            "max_drawdown": safe_value(risk["max_drawdown"]),
        }
    }

    ai_result = run_crew(summary)

    price_history = {
        "dates": df.index.to_series().dt.strftime("%Y-%m-%d").tolist(),
        "close": safe_list(
            close_series.astype(float).round(2).tolist()
        ),
        "sma_20": safe_list(
            close_series
            .rolling(20)
            .mean()
            .astype(float)
            .round(2)
            .tolist()
        )
    }

    return {
        "market_data": summary,
        "price_history": price_history,
        "ai_decision": ai_result
    }
