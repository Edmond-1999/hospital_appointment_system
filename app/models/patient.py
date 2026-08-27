from pydantic import BaseModel, Field
from app.models.user import User
from app.models.enums import AppointmentStatus
from uuid import UUID, uuid4
from datetime import datetime, timezone

class Patient(User):
        # def __init__(self, _id: int, fullname: str, email: str, phone: str, password: str,
        #              date_of_birth: str, gender: str, address: str, reason: str):
    id = int
    date_of_birth = str
    appointment_id = str
    appointment_status = str
    gender = str
    address = str
    reason = str
    appointments = str

    def role(self) -> str:
        return "Patient"

    def book_appointment(self, appointment) -> None:
        self.appointments.append(appointment)

    def view_appointments(self) -> list:
        return self.appointments

    def cancel_appointment(self, appointment_id: int) -> None:
        self.appointments = [
            a for a in self.appointments if a.appointment_id != appointment_id
        ]

