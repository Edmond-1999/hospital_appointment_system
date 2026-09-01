from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from app.models.appointment_status import AppointmentStatus


class BookAppointmentRequest(BaseModel):
    department:str
    description:str
    appointment_datetime: datetime


class BookAppointmentResponse(BaseModel):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    doctor_name: str
    department: str
    description: str
    appointment_datetime: datetime
    status: AppointmentStatus