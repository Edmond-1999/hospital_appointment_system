from uuid import UUID

from app.models.user import User
from app.models.user_role import UserRole


class Doctor(User):
    role: UserRole = UserRole.DOCTOR
    specialization: str
    department_id: UUID | None = None