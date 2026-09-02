from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.models.user_role import UserRole


class DoctorCreate(BaseModel):
    fullname: str
    email: EmailStr
    phone: str
    password: str
    specialization: str
    department: str


class DoctorResponse(BaseModel):
    id: UUID
    fullname: str
    email: EmailStr
    phone: str
    specialization: str
    department: str
    role: UserRole

class DoctorRead(BaseModel):
    user_id = UUID
    fullname = str
    email = EmailStr
    phone = str
    password = str
    specialization = str
    department = str