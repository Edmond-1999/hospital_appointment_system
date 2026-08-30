from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import AppointmentStatus


class BookAppointmentRequest(BaseModel):
    department_id: UUID
    appointment_datetime: datetime


class BookAppointmentResponse(BaseModel):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    department_id: UUID
    appointment_datetime: datetime
    status: AppointmentStatus


class UpdateAppointmentStatusRequest(BaseModel):
    status: AppointmentStatus


