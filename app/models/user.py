from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from app.models.user_role import UserRole

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    fullname: str
    email: str
    phone: str
    password: str
    role: UserRole
