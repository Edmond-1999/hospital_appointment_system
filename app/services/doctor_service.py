from uuid import uuid4, UUID

from app.exceptions import ConflictError, NotFoundError
from app.models.doctor import Doctor
from app.models.user import User
from app.models.user_role import UserRole
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate


class DoctorService:
    def __init__(self, repository: DoctorRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def create_doctor(self, payload: DoctorCreate) -> Doctor:
        if self.user_repository.get_user_by_email(payload.email):
            raise ConflictError(
                f"An account with email {payload.email} already exists!"
            )

        user = User(
            id = uuid4(),
            fullname = payload.fullname,
            email = payload.email,
            phone = payload.phone,
            password = payload.password,
            role = UserRole.DOCTOR
        )
        self.user_repository.add_user(user)

        doctor = Doctor(
            id = user.id,
            fullname = user.fullname,
            email = user.email,
            phone = user.phone,
            password = user.password,
            role = UserRole.DOCTOR,
            specialization = payload.specialization,
            department_id = payload.department_id
        )

        return self.repository.add_doctor(doctor)

    def get_doctor(self, doctor_id: UUID) -> Doctor:
        doctor = self.repository.get_doctor(doctor_id)

        if doctor is None:
            raise NotFoundError(f"Doctor with id {doctor_id} not found!")

        return doctor

    def list_doctors(self) -> list[Doctor]:
        return self.repository.list_doctors()

    def update_doctor(self, doctor_id: UUID, payload: DoctorUpdate) -> Doctor:
        doctor = self.get_doctor(doctor_id)

        email = payload.email

        if email is not None and email != doctor.email:

            if self.user_repository.get_user_by_email(email):
                raise ConflictError(f"An account with email {email} already exists!")

        data = payload.model_dump(exclude_unset = True)

        updated = self.repository.update_doctor(doctor_id, data)

        if updated is None:
            raise NotFoundError(f"Doctor with id {doctor_id} not found!")

        return updated

    def delete_doctor(self, doctor_id: UUID) -> None:
        self.get_doctor(doctor_id)

        self.repository.delete_doctor(doctor_id)
