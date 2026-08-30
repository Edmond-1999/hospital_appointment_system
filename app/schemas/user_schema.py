from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    fullname: str
    email: str
    phone: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    fullname: str
    email: str
    phone: str

class LoginResponse(BaseModel):
    message: str


class LogoutRequest(BaseModel):
    email: str


class LogoutResponse(BaseModel):
    message: str