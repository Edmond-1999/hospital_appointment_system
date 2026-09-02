from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field as SQLField

from app.models.user_role import UserRole

class User(SQLModel, table=True):
    id: UUID = SQLField(default_factory=uuid4, primary_key=True)
    fullname: str = SQLField(index=True)
    email: str = SQLModel(unique=True, index=True)
    phone: str = SQLField(...)
    password: str = SQLField(min_length=8, max_length=15)
    role: UserRole
