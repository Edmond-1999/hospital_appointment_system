import datetime
from uuid import UUID

from pydantic import BaseModel


class DoctorAvailabilityCreate(BaseModel):
    doctor_id: UUID
    available_date: datetime


class DoctorAvailabilityResponse(BaseModel):
    id: UUID
    doctor_id: UUID
    available_date: datetime