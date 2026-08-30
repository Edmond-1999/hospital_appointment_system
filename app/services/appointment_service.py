from datetime import datetime
from uuid import UUID

from app.models.appointment import Appointment
from app.models.enums import AppointmentStatus
from repositories.appointment_repository import AppointmentRepository
from repositories.in_memory_repository import InMemoryRepository


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def create_appointment(self, patient_id: UUID, department_id:UUID, appointment_datetime: datetime ) -> Appointment:
        pass

    def get_patient_appointments(self, patient_id: UUID) -> list[Appointment]:
        pass

    def cancel_appointment(self, appointment_id: UUID, user_id: UUID) -> None:
        pass

    def confirm_appointment(self, appointment_id: UUID, doctor_id:UUID) -> None:
        pass

    def complete_appointment(self, appointment_id: UUID, doctor_id :UUID) -> None:
        pass