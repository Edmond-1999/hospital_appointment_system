from datetime import date
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class PatientCreate(BaseModel):
    fullname: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=15)
    phone: str
    date_of_birth: date
    gender: str
    address: str

class PatientRead(BaseModel):
    user_id: UUID
    fullname: str
    email: EmailStr
    phone: str
    date_of_birth: date
    gender: str
    address: str
