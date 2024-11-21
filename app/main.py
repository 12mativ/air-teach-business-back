from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

class CourseBody(BaseModel):
  courseDates: dict[str, datetime]
  courseTheme: str

class LecturerBody(BaseModel):
  first_name: str
  last_name: str
  specialization: str
  description: str

app = FastAPI()

@app.post("/create-shedule")
async def create_shedule(body: CourseBody) -> CourseBody:
  return body

@app.post("/create-lecturer", status_code=status.HTTP_201_CREATED)
async def create_lecturer(body: LecturerBody):
  return body
  