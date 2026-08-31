from uuid import UUID

from pydantic import BaseModel, Field, EmailStr
from app.models.user_role import UserRole


class UserCreate(BaseModel):
    fullname: str
    email: EmailStr
    phone: str
    password: str = Field(min_length=8, max_length=15)


class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    fullname: str
    email: EmailStr
    phone: str
    role: UserRole

class LoginResponse(BaseModel):
    message: str


class LogoutRequest(BaseModel):
    email: str


class LogoutResponse(BaseModel):
    message: str