
from datetime import datetime
from uuid import UUID, uuid4


from sqlmodel import SQLModel, Field

from app.models.appointment_status import AppointmentStatus


class Appointment(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    patient_id: UUID
    doctor_id: UUID
    doctor_name: str
    department: str
    description: str
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