from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.patient_repository import PatientRepository


class DoctorService:
    def __init__(self, doctor_repository: DoctorRepository, appointment_repository: AppointmentRepository, patient_repository: PatientRepository):
        self.doctor_repository = doctor_repository
        self.appointment_repository = appointment_repository
        self.patient_repository = patient_repository