from fastapi import APIRouter, status
from pydantic import BaseModel

lecturer_router = APIRouter(
  prefix="/lecturers",
  tags=["lecturers"]
)

class LecturerBody(BaseModel):
  first_name: str
  last_name: str
  specialization: str
  description: str | None

lecturer_array: list[LecturerBody] = []

@lecturer_router.post("/create-lecturer", status_code=status.HTTP_201_CREATED)
async def create_lecturer(body: LecturerBody):
  lecturer_array.append(body)
  return {"lecturer": body} 

@lecturer_router.post("/create-lecturer", status_code=status.HTTP_201_CREATED)
async def create_lecturer(body: LecturerBody):
  lecturer_array.append(body)
  return {"lecturer": body} 