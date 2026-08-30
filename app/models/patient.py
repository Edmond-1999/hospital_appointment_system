from datetime import date
from typing import Optional
from app.models.user import User
from app.models.user_role import UserRole


class Patient(User):
    role: UserRole = UserRole.PATIENT
    date_of_birth: date
    gender: str
    address: str
    reason: Optional[str] = None
