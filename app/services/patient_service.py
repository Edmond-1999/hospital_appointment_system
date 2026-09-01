from datetime import datetime
from uuid import UUID

from app.services.appointment_service import AppointmentService

class PatientService:
    def __init__(self, appointment_service: AppointmentService):
        self.appointment_service = appointment_service


    def book_appointment(self, patient_id: UUID, department_id: UUID, appointment_datetime: datetime):
        return self.appointment_service.create_appointment(patient_id, department_id, appointment_datetime)

    def view_appointments(self, patient_id: UUID):
        return self.appointment_service.get_patient_appointments(patient_id)

    def cancel_appointment(self, patient_id: UUID, appointment_id: UUID):
        return self.appointment_service.cancel_appointment(appointment_id, patient_id)