from fastapi import FastAPI
from .lecturer.router import lecturer_router
from .schedule.router import schedule_router
from .auth.router import auth_router

app = FastAPI()

app.include_router(auth_router)

app.include_router(lecturer_router)

app.include_router(schedule_router)