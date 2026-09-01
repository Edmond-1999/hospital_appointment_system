from uuid import UUID

from pydantic import BaseModel

from app.models.user_role import UserRole


class DoctorCreate(BaseModel):
    fullname: str
    email: str
    password: str
    phone: str
    specialization: str
    department: str


class DoctorResponse(BaseModel):
    id: UUID
    fullname: str
    email: str
    phone: str
    specialization: str
    department: str
    role: UserRole