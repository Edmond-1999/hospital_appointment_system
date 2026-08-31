from datetime import date

from app.models.user import User

class Patient(User):
    date_of_birth: date
    gender: str
    address: str