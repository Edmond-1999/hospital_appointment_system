import datetime
import uuid
from uuid import UUID, uuid4

from pydantic import Field


class DoctorAvailability:
    id: UUID = Field(default_factory=uuid.uuid4)
    doctor_id: UUID
    available_date: datetime