from uuid import uuid4, UUID
from pydantic import BaseModel, Field

from app.models.enums import UserRole

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    fullname: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    password: str = Field(...)
    role: UserRole = Field(...)

    def login(self, email: str, password: str):
        return self.email == email.lower() and self.password == password

    def logout(self, email:str) -> None:
        return self.email.lower() == email.lower()

