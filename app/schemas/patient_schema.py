from typing import Optional
from datetime import date
from  app.schemas.user_schema import UserCreate, UserUpdate, UserRead

class PatientCreate(UserCreate):
    date_of_birth: date
    gender: str
    address: str
    reason: Optional[str] = None

class PatientUpdate(UserUpdate):
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    reason: Optional[str] = None

class PatientRead(UserRead):
    date_of_birth: date
    gender: str
    address: str
    reason: Optional[str] = None




