from fastapi import APIRouter, status
from pydantic import BaseModel
from datetime import datetime, date
from ..lecturer.models import LecturerBody
from utils.org_lecturers_chat import create_schedule

test_lecturers: list[LecturerBody] = [
  {
    "first_name": "Ivan",
    "last_name": "Matukhin",
    "specialization": "cakes",
    "description": "i am perfect at making cakes. i have free time on monday (STRONGLY ONLY MONDAY) from 10am to 1pm, tuesday (STRONGLY ONLY TUESDAY) from 3pm to 5pm for giving lectures"
  },
  {
    "first_name": "Petr",
    "last_name": "Petrov",
    "specialization": "cakes",
    "description": "i am perfect at making cakes. i have free time on monday (STRONGLY ONLY MONDAY) from 9am to 1pm, tuesday (STRONGLY ONLY TUESDAY) from 3pm to 6pm for giving lectures"
  }
]

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
async def create_shedule(body: CourseModel):
  # получение необходимых лекторов по теме курса
  create_schedule(test_lecturers)
  return body