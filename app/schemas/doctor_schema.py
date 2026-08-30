from typing import Optional
from uuid import UUID

from app.schemas.user_schema import UserCreate, UserUpdate, UserRead


class DoctorCreate(UserCreate):
    specialization: str
    department_id: Optional[UUID] = None

class DoctorUpdate(UserUpdate):
    specialization: Optional[str] = None
    department_id: Optional[UUID] = None

class DoctorRead(UserRead):
    specialization: str
    department_id: Optional[UUID] = None