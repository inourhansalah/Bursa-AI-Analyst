def make_ai_decision(data: dict) -> str:
    if data["rsi"] < 30:
        return "BUY"
    elif data["rsi"] > 70:
        return "SELL"
    else:
        return "HOLD"
