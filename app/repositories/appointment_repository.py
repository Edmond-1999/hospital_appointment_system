from datetime import datetime
from uuid import UUID

from app.models.appointment import Appointment
from app.repositories.in_memory_repository import InMemoryRepository


class AppointmentRepository(InMemoryRepository[Appointment]):
    def find_by_patient(self, patient_id: UUID) -> list[Appointment]:

        appointments = []
        for appointment in self._items.values():
            if appointment.patient_id == patient_id:
                appointments.append(appointment)

        return appointments

    def find_doctor_by_datetime(self, doctor_id:UUID, appointment_datetime: datetime) -> Appointment | None:
        for appointment in self._items.values():
            if appointment.doctor_id == doctor_id and appointment.appointment_datetime == appointment_datetime:

                return appointment
        return None

    def find_by_doctor(self, doctor_id: UUID) -> list[Appointment]:
        appointments = []

        for appointment in self._items.values():
            if appointment.doctor_id == doctor_id:
                appointments.append(appointment)

        return appointments
