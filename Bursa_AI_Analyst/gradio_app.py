import gradio as gr
import requests
import plotly.graph_objects as go
import pandas as pd

API_URL = "http://127.0.0.1:8000/analyze-stock"

# ================== Helpers ==================

def safe_display(value):
    return value if value is not None else "N/A"


def summarize_text(text, max_sentences=3):
    if not text:
        return "No AI analysis available."
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + "."


# ================== Charts ==================

def price_chart(history):
    df = pd.DataFrame({
        "date": history["dates"],
        "close": history["close"],
        "sma_20": history["sma_20"]
    })

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["close"],
        mode="lines",
        name="Close Price"
    ))

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["sma_20"],
        mode="lines",
        name="SMA 20"
    ))

    fig.update_layout(
        title="📈 Price & SMA 20",
        xaxis_title="Date",
        yaxis_title="Price",
        hovermode="x unified"
    )

    return fig


def rsi_chart(history):
    close = pd.Series(history["close"]).dropna()

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=rsi,
        mode="lines",
        name="RSI"
    ))

    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")

    fig.update_layout(
        title="📉 RSI Indicator",
        yaxis_title="RSI",
        hovermode="x unified"
    )

    return fig


# ================== Main Logic ==================

def analyze(ticker, period, analysis_mode):
    r = requests.post(
        API_URL,
        params={"ticker": ticker, "period": period},
        timeout=60
    )

    if r.status_code != 200:
        return "❌ API Error", r.text, None, None

    data = r.json()

    market = data["market_data"]
    history = data["price_history"]
    ai_decision = data["ai_decision"]

    market_text = (
        f"📊 Close Price: {safe_display(market['close_price'])}\n"
        f"📉 RSI: {safe_display(market['rsi'])}\n"
        f"📈 SMA 20: {safe_display(market['sma_20'])}\n\n"
        f"⚠️ Volatility: {safe_display(market['risk']['volatility'])}\n"
        f"📉 Max Drawdown: {safe_display(market['risk']['max_drawdown'])}"
    )

    ai_raw = ai_decision.get("raw", "")
    ai_text = (
        summarize_text(ai_raw)
        if analysis_mode == "Short Summary"
        else ai_raw
    )

    return (
        market_text,
        ai_text,
        price_chart(history),
        rsi_chart(history)
    )


# ================== UI ==================

with gr.Blocks(title="📈 Bursa AI Analyst") as app:
    gr.Markdown("# 📈 Bursa AI Analyst")
    gr.Markdown("### AI‑Powered Stock Analysis with CrewAI & Interactive Charts")

    ticker = gr.Dropdown(
        label="Choose a Stock",
        choices=[
            "AAPL", "MSFT", "GOOGL", "AMZN", "META",
            "TSLA", "NVDA", "NFLX"
        ],
        value="AAPL"
    )

    with gr.Row():
        period = gr.Dropdown(
            ["1mo", "3mo", "6mo", "1y"],
            value="1y",
            label="Period"
        )

        analysis_mode = gr.Radio(
            ["Full AI Analysis", "Short Summary"],
            value="Full AI Analysis",
            label="AI Output Mode"
        )

    analyze_btn = gr.Button("🔍 Analyze Stock")

    with gr.Row():
        market_out = gr.Textbox(label="📊 Market Data", lines=8)
        ai_out = gr.Textbox(label="🤖 AI Analysis", lines=15)

    price_plot = gr.Plot(label="📈 Price & SMA 20")
    rsi_plot = gr.Plot(label="📉 RSI Indicator")

    gr.Markdown("### 📘 Metrics Explained")
    gr.Markdown(
        """
**📊 Close Price** – Last traded price at the end of the period.  
**📉 RSI** – Momentum indicator (below 30 = oversold, above 70 = overbought).  
**📈 SMA 20** – 20‑day average price (trend direction).  
**⚠️ Volatility** – Measures price fluctuation (risk).  
**📉 Max Drawdown** – Worst historical loss from a peak.
        """
    )

    analyze_btn.click(
        analyze,
        inputs=[ticker, period, analysis_mode],
        outputs=[market_out, ai_out, price_plot, rsi_plot]
    )

app.launch()
