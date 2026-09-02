from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: str
    role: str

class LogoutRequest(BaseModel):
    email: EmailStr

class LogoutResponse(BaseModel):
    message: str