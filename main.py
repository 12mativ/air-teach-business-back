from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Body(BaseModel):
  courseDates: dict[str, datetime]
  courseTheme: str

app = FastAPI()


@app.post("/create-shedule")
async def root(body: Body) -> Body:
  return body