from uuid import uuid4, UUID
from pydantic import Field
from sqlmodel import SQLModel, Field as SQLField

from app.models.user_role import UserRole

class User(SQLModel, table=True):
    id: UUID = SQLField(default_factory=uuid4, primary_key=True)
    fullname: str = SQLField(index=True)
    email: str = SQLModel(unique=True, index=True)
    phone: str = Field(...)
    password: str = Field(min_length=8, max_length=15)
    role: UserRole

    def login(self, email: str, password: str):
        return self.email == email.lower() and self.password == password

    def logout(self, email:str) -> bool:
        return self.email.lower() == email.lower()