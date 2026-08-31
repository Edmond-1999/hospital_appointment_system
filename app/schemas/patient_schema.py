from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from app.models.user_role import UserRole


class PatientCreate(BaseModel):
    fullname: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=15)
    phone: str


class PatientResponse(BaseModel):
    id: UUID
    fullname: str
    email: str
    phone: str
    role: UserRole