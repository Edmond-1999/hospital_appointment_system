from app.repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def create_appointment(self, patient_id, department_id, appointment_datetime):
        # use self.appointment_repository to persist the appointment
        pass

    def get_patient_appointments(self, patient_id):
        # use self.appointment_repository to fetch appointments
        pass

    def cancel_appointment(self, appointment_id, patient_id):
        # use self.appointment_repository to cancel
        pass
    
    
    
    