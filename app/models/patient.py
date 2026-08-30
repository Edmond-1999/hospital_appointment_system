from datetime import date
from uuid import UUID

from app.models.user import User

class Patient(User):
    date_of_birth: date
    gender: str
    address: str
