from datetime import datetime
from uuid import UUID

from app.models.user import User

class Patient(User):
    date_of_birth: datetime
    gender: str
    address: str

    def book_appointment(self, department_id:UUID, appointment_date: datetime) -> None:
        pass

    def view_appointments(self) -> list:
        pass

    # def view_appointments(self) -> list:
    #     pass

    def cancel_appointment(self, appointment_id:UUID) -> None:
        pass