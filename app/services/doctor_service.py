from uuid import UUID

from app.models.user import User
from app.models.user_role import UserRole
from app.repositories.user_repository import UserRepository
from app.repositories.doctor_repository import DoctorRepository

from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorRead
from app.services.appointment_service import AppointmentService


class DoctorService:

    def __init__(self, appointment_service: AppointmentService, user_repository: UserRepository, doctor_repository: DoctorRepository):
        self.appointment_service = appointment_service
        self.user_repository = user_repository
        self.doctor_repository = doctor_repository

    def register(self, data: DoctorCreate) -> DoctorRead:
        if self.user_repository.find_by_email(data.email) is not None:
            raise ValueError("Doctor already exists")

        user = User(
            fullname=data.fullname,
            email=data.email,
            phone=data.phone,
            password=data.password,
            role=UserRole.DOCTOR,
        )

        self.user_repository.create(user)

        doctor = Doctor(
            user_id = user.id,
            specialization = data.specialization,
            department = data.department
        )

        self.doctor_repository.create(doctor)

        return DoctorRead(
            user_id=doctor.id,
            fullname = user.fullname,
            email = user.email,
            phone = user.phone,
            password = user.password,
            specialization = doctor.specialization,
            department = doctor.department
        )




    def view_appointments(self, doctor_id: UUID):
        return self.appointment_service.view_doctor_appointments(doctor_id)


    def change_status(self, appointment_id: UUID,status: str):
        return self.appointment_service.change_status(appointment_id,status)
