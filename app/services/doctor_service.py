from uuid import UUID

from services.appointment_service import AppointmentService


class DoctorService:
    def __init__(self, appointment_service: AppointmentService):
        self.appointment_service = appointment_service

    def view_appointments(self, doctor_id: UUID):
        # return self.appointment_service.get_doctor_appointments(doctor_id)
        pass

    def view_patient(self, patient_id: UUID):
        # return self.appointment_service.get_patient(patient_id)
        pass

    def change_status(self,appointment_id: UUID, status):
        # return self.appointment_service.change_status(appointment_id, status)
        pass
