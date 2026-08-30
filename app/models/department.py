from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.doctor import Doctor

class Department(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def add_doctor(self, department_id: UUID, doctor: Doctor) -> None:
        pass

    def remove_doctor(self, department_id: UUID, doctor: Doctor) -> None:
        pass

    def get_doctors(self, department_id:UUID) -> list[Doctor]:
        pass