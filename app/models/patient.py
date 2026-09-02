from datetime import date
from sqlmodel import SQLModel, Field as SQLField
from uuid import UUID

class Patient(SQLModel, table=True):
    __tablename__ = 'patient'
    user_id: UUID = SQLField(foreign_key="user.id", primary_key=True)
    date_of_birth: date
    gender: str
    address: str