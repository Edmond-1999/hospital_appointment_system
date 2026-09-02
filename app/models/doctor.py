from uuid import UUID

from sqlmodel import SQLModel, Field as SQLField




class Doctor(SQLModel, table=True):
    __tablename__ = "doctor"

    user_id : UUID = SQLField(foreign_key="user.id", primary_key=True)
    specialization: str
    department: str