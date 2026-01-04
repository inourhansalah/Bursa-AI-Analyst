from crewai import Task
from app.crew.agents import market_agent, risk_agent, decision_agent

def create_tasks(summary: dict):
    market_task = Task(
        description=(
            f"Analyze the market trend and technical indicators "
            f"for the following stock data: {summary}"
        ),
        agent=market_agent,
        expected_output="Bullish, bearish, or neutral trend with reasoning."
    )

    risk_task = Task(
        description=(
            f"Evaluate the investment risk based on this data: {summary}"
        ),
        agent=risk_agent,
        expected_output="Low, Medium, or High risk with explanation."
    )

    decision_task = Task(
        description=(
            "Based on the market analysis and risk assessment, "
            "decide whether the stock is a Buy, Hold, or Sell."
        ),
        agent=decision_agent,
        expected_output="Final Buy/Hold/Sell decision with justification."
    )

    return [market_task, risk_task, decision_task]
