import os
from dotenv import load_dotenv
from crewai import Agent

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

market_agent = Agent(
    role="Market Analyst",
    goal="Analyze stock price trends and technical indicators",
    backstory="Expert in financial markets and technical analysis",
    verbose=True
)

risk_agent = Agent(
    role="Risk Analyst",
    goal="Evaluate investment risk using volatility and drawdown",
    backstory="Expert in financial risk management",
    verbose=True
)

decision_agent = Agent(
    role="Investment Advisor",
    goal="Make Buy, Hold, or Sell decisions based on analysis",
    backstory="Professional investment advisor",
    verbose=True
)
