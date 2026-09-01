from uuid import UUID

from app.services.appointment_service import AppointmentService


class DoctorService:
    def __init__(self, appointment_service: AppointmentService):
        self.appointment_service = appointment_service

    def view_appointments(self, doctor_id: UUID):
        return self.appointment_service.get_patient_appointments(doctor_id)

    def view_patient(self, patient_id: UUID):
        return self.appointment_service.get_patient(patient_id)
