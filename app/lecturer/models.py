from pydantic import BaseModel

class LecturerBody(BaseModel):
  first_name: str
  last_name: str
  specialization: str
  description: str | None