from crewai import Crew
from app.crew.tasks import create_tasks

def run_crew(summary: dict):
    tasks = create_tasks(summary)
    crew = Crew(tasks=tasks)
    result = crew.kickoff()
    return result
