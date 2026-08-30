from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.enums import AppointmentStatus

class Appointment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    doctor_id: UUID
    department_id: UUID
    appointment_datetime: datetime
    status: AppointmentStatus = AppointmentStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


    def confirm(self) -> None:
        self.status = AppointmentStatus.CONFIRMED
    def complete(self) -> None:
        self.status = AppointmentStatus.COMPLETED
    def cancel(self) -> None:
        self.status = AppointmentStatus.CANCELLED


