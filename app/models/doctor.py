from uuid import UUID

from app.models.user import User
from app.models.enums import AppointmentStatus


class Doctor(User):
    specialization_id: str
    department_id: UUID

