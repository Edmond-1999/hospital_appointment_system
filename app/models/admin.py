from uuid import UUID
from sqlmodel import SQLModel, Field as SQLField

class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    user_id: UUID = SQLField(foreign_key="user.id", primary_key=True)
    department: str