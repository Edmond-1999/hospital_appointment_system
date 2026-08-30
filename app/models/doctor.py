from uuid import UUID

from app.models.user import User
from app.models.enums import AppointmentStatus


class Doctor(User):
    specialization_id: str
    department_id: UUID


    def view_appointments(self) -> list:
        pass

    def manage_appointment(self) -> None:
        pass

    def view_patients(self) -> list:
        pass

    def change_status(self, appointment_id:UUID, status: AppointmentStatus) -> None:
        pass