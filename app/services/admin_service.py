from uuid import UUID

from app.repositories.user_repository import UserRepository
from app.repositories.admin_repository import AdminRepository
from app.repositories.patient_repository import PatientRepository
from app.repositories.doctor_repository import DoctorRepository
from app.services.appointment_service import AppointmentService

from app.schemas.admin_schema import AdminCreate, AdminRead, UserSummary, DeleteUserResponse
from app.models.user import User
from app.models.admin import Admin
from app.models.user_role import UserRole


class AdminService:
    def __init__(
        self,
        user_repository: UserRepository,
        admin_repository: AdminRepository,
        patient_repository: PatientRepository,
        doctor_repository: DoctorRepository,
        appointment_service: AppointmentService,
    ):
        self.user_repository = user_repository
        self.admin_repository = admin_repository
        self.patient_repository = patient_repository
        self.doctor_repository = doctor_repository
        self.appointment_service = appointment_service

    def register(self, data: AdminCreate) -> AdminRead:
        if self.user_repository.find_by_email(data.email) is not None:
            raise ValueError("User already exists")

        user = User(
            fullname=data.fullname,
            email=data.email,
            phone=data.phone,
            password=data.password,
            role=UserRole.ADMIN,
        )
        self.user_repository.create(user)

        admin = Admin(user_id=user.id, department=data.department)
        self.admin_repository.create(admin)

        return AdminRead(
            user_id=admin.user_id,
            fullname=user.fullname,
            email=user.email,
            phone=user.phone,
            department=admin.department,
        )

    def list_all_users(self) -> list[UserSummary]:
        users = self.user_repository.find_all()
        return [
            UserSummary(
                id=user.id,
                fullname=user.fullname,
                email=user.email,
                phone=user.phone,
                role=user.role.value,
            )
            for user in users
        ]

    def view_patient_appointments(self, patient_id: UUID):
        return self.appointment_service.get_patient_appointments(patient_id)

    # app/services/admin_service.py
    def delete_user(self, user_id: UUID) -> DeleteUserResponse:
        user = self.user_repository.find_by_id(user_id)
        if user is None:
            raise ValueError("User not found")

        deleted_id = user.id
        deleted_fullname = user.fullname

        if user.role == UserRole.PATIENT:
            patient = self.patient_repository.find_by_id(user_id)
            if patient is not None:
                self.patient_repository.delete(patient)
        elif user.role == UserRole.DOCTOR:
            doctor = self.doctor_repository.find_by_id(user_id)
            if doctor is not None:
                self.doctor_repository.delete(doctor)
        elif user.role == UserRole.ADMIN:
            admin = self.admin_repository.find_by_id(user_id)
            if admin is not None:
                self.admin_repository.delete(admin)

        self.user_repository.delete(user)

        return DeleteUserResponse(
            id=deleted_id,
            fullname=deleted_fullname,
            message=f"User '{deleted_fullname}' was successfully deleted",
        )

