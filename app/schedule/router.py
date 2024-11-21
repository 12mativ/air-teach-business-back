from fastapi import APIRouter, status
from pydantic import BaseModel
from datetime import datetime, date

schedule_router = APIRouter(
  prefix="/schedule",
  tags=["schedule"]
)

class CourseModel(BaseModel):
  courseDates: dict[str, datetime]
  courseTheme: str

class ScheduleModel(BaseModel):
  # пример струтуры schedule
  # [
  #   {
  #     "2024-11-22": [
  #       {"start": 2024-11-21T20:52:05+00:00, "end": 2024-11-21T20:55:05+00:00}
  #     ]
  #   }
  # ]
  shedule: list[dict[date, dict[str, datetime]]]

@schedule_router.post("/create-schedule", status_code=status.HTTP_201_CREATED)
async def create_shedule(body: CourseModel) -> ScheduleModel:
  # получение необходимых лекторов по теме курса
  # составление расписания
  return body