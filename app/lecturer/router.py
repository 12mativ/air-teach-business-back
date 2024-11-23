from fastapi import APIRouter, status
from .models import LecturerBody

lecturer_router = APIRouter(
  prefix="/lecturers",
  tags=["lecturers"]
)

lecturer_array: list[LecturerBody] = []

@lecturer_router.post("/create-lecturer", status_code=status.HTTP_201_CREATED)
async def create_lecturer(body: LecturerBody):
  lecturer_array.append(body)
  return {"lecturer": body}