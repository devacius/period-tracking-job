from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    email: EmailStr
    first_period_date: date
    cycle_length: int = 28
    name:str

class PeriodPrediction(BaseModel):
    next_period_start: date
    fertile_window: list[date]
