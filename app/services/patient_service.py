from datetime import datetime
from uuid import UUID
from app.repositories.user_repository import UserRepository
from app.repositories.patient_repository import PatientRepository
from app.services.appointment_service import AppointmentService
from app.schemas.patient_schema import PatientCreate, PatientRead
from app.models.user import User
from app.models.patient import Patient
from app.models.user_role import UserRole

class PatientService:
    def __init__(self, user_repository: UserRepository, patient_repository: PatientRepository, appointment_service: AppointmentService,):
        self.user_repository = user_repository
        self.patient_repository = patient_repository
        self.appointment_service = appointment_service

    def register(self, data: PatientCreate) -> PatientRead:
        if self.user_repository.find_by_email(data.email) is not None:
            raise ValueError("User already exists")

        user = User(
            fullname=data.fullname,
            email=data.email,
            phone=data.phone,
            password=data.password,
            role=UserRole.PATIENT,
        )
        self.user_repository.create(user)

        patient = Patient(
            user_id=user.id,
            date_of_birth=data.date_of_birth,
            gender=data.gender,
            address=data.address,
        )
        self.patient_repository.create(patient)

        return PatientRead(
            user_id=patient.user_id,
            fullname=user.fullname,
            email=user.email,
            phone=user.phone,
            date_of_birth=patient.date_of_birth,
            gender=patient.gender,
            address=patient.address,
        )

    def book_appointment(self, patient_id: UUID, department_name: str, appointment_datetime: datetime, description: str):
        return self.appointment_service.create_appointment(patient_id, department_name, appointment_datetime, description)

    def view_appointments(self, patient_id: UUID):
        return self.appointment_service.get_appointments_status(patient_id)

    def cancel_appointment(self, patient_id: UUID, appointment_id: UUID):
        return self.appointment_service.cancel_appointment(appointment_id, patient_id)