from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Bursa AI Analyst")

app.include_router(router)
