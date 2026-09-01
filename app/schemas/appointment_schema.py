from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class BookAppointmentRequest(BaseModel):
    department_id: UUID
    appointment_datetime: datetime


class BookAppointmentResponse(BaseModel):
    id: UUID
    patient_id: UUID
    department_id: UUID
    appointment_datetime: datetime
    status: str