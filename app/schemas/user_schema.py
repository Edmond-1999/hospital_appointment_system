from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict
from app.models.user_role import UserRole
from typing import Optional

class UserBase(BaseModel):
    fullname: str
    email: str
    phone: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    fullname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None

class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(default_factory=uuid4)
    role: UserRole

