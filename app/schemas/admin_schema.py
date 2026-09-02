from uuid import UUID
from pydantic import BaseModel, EmailStr


class AdminCreate(BaseModel):
    fullname: str
    email: EmailStr
    phone: str
    password: str
    department: str


class AdminRead(BaseModel):
    user_id: UUID
    fullname: str
    email: EmailStr
    phone: str
    department: str


class UserSummary(BaseModel):
    id: UUID
    fullname: str
    email: EmailStr
    phone: str
    role: str

class DeleteUserResponse(BaseModel):
    id: UUID
    fullname: str
    message: str