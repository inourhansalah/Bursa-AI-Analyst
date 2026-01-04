#  Bursa AI Analyst

An **AI-powered stock analysis system** that combines **financial indicators**, **risk analysis**, and **LLM-based reasoning** using **CrewAI**, with an interactive **Gradio dashboard** and a **FastAPI backend**.

This project demonstrates how **Large Language Models (LLMs)** can collaborate as **multiple AI agents** to produce **human-like investment analysis**, not just raw numbers.

---

##  Features

-  Real-time stock market data (Yahoo Finance)
-  Technical indicators (RSI, SMA 20)
-  Risk metrics (Volatility, Max Drawdown)
-  Multi-agent AI reasoning using **CrewAI**
-  LLM-powered Buy / Hold / Sell analysis
-  Interactive charts (Price + SMA, RSI)
-  Clean and simple Gradio UI
-  FastAPI backend (scalable & production-ready)

---

##  System Architecture
User (Gradio UI)
↓
FastAPI Backend (/analyze-stock)
↓
Yahoo Finance (Market Data)
↓
Indicators + Risk Calculation
↓
CrewAI (LLM Agents)
↓
AI Decision & Explanation
↓
Gradio Dashboard (Charts + Text)

---

##  Project Structure
Bursa_AI_Analyst/
│
├── app/
│ ├── api/
│ │ └── routes.py # FastAPI endpoint
│ │
│ ├── services/
│ │ ├── market_data.py # Fetch stock data
│ │ ├── indicators.py # RSI, SMA calculations
│ │ └── risk.py # Volatility & drawdown
│ │
│ ├── crew/
│ │ ├── agents.py # CrewAI agents
│ │ ├── tasks.py # CrewAI tasks
│ │ └── crew.py # Crew execution
│ │
│ └── main.py # FastAPI app entry point
│
├── gradio_app.py # Gradio UI
├── requirements.txt
├── .env # OpenAI API key
└── README.md


---


---

##  AI & CrewAI Explained

###  What is CrewAI?
CrewAI allows multiple **LLM agents** to collaborate, each with a **specific role**, similar to a real investment team.

###  Agents Used

1. **Market Analyst**
   - Analyzes price trends and technical indicators
   - Focuses on RSI and SMA

2. **Risk Analyst**
   - Evaluates volatility and maximum drawdown
   - Assesses downside risk

3. **Investment Advisor**
   - Combines market and risk analysis
   - Produces final **Buy / Hold / Sell** decision with explanation

Each agent uses an **LLM** to reason in **natural language**, not simple `if/else` logic.

---

##  Technical Indicators

| Indicator | Description |
|---------|------------|
| Close Price | Last traded price |
| RSI | Momentum indicator (Oversold < 30, Overbought > 70) |
| SMA 20 | 20-day moving average (trend direction) |
| Volatility | Measures price fluctuation (risk) |
| Max Drawdown | Worst historical loss from a peak |

---

##  Gradio Dashboard

The Gradio UI allows users to:

- Choose a stock ticker
- Select analysis period
- Toggle AI output:
  - Full analysis
  - Short summary
- View:
  - Market metrics
  - AI reasoning
  - Interactive charts

###  Charts Included
- Price + SMA 20
- RSI with overbought/oversold levels

---

