from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field as SQLField
from app.models.appointment_status import AppointmentStatus


class Appointment(SQLModel, table=True):
    id: UUID = SQLField(default_factory=uuid4, primary_key=True)
    patient_id: UUID
    doctor_id: UUID
    doctor_name: str
    department: str
    description: str
    appointment_datetime: datetime
    status: AppointmentStatus = SQLField(default = AppointmentStatus.PENDING)
    created_at: datetime = SQLField(default_factory=datetime.now)
    updated_at: datetime = SQLField(default_factory=datetime.now)


    def confirm(self) -> None:
        self.status = AppointmentStatus.CONFIRMED
        self.updated_at = datetime.now()

    def complete(self) -> None:
        self.status = AppointmentStatus.COMPLETED
        self.updated_at = datetime.now()

    def cancel(self) -> None:
        self.status = AppointmentStatus.CANCELLED
        self.updated_at = datetime.now()