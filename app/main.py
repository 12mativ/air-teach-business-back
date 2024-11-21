from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime
from .lecturer import router

class CourseBody(BaseModel):
  courseDates: dict[str, datetime]
  courseTheme: str

app = FastAPI()

app.include_router(router.router)

@app.post("/create-shedule")
async def create_shedule(body: CourseBody) -> CourseBody:
  return body