from uuid import UUID, uuid4

from app.schemas.patient_schema import PatientCreate, PatientUpdate
from app.exceptions import ConflictError, NotFoundError
from app.models.patient import Patient
from app.models.user import User
from app.models.user_role import UserRole
from app.repositories.patient_repository import PatientRepository
from app.repositories.user_repository import UserRepository


class PatientService:
    def __init__(self, repository: PatientRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def create_patient(self, payload: PatientCreate) -> Patient:
        if self.user_repository.get_user_by_email(payload.email):
            raise ConflictError(f"An account with email '{payload.email}' already exists")

        user = User(
            id=uuid4(),
            fullname=payload.fullname,
            email=payload.email,
            phone=payload.phone,
            password=payload.password,
            role=UserRole.PATIENT,
        )
        self.user_repository.add_user(user)

        patient = Patient(
            id=user.id,
            role=UserRole.PATIENT,
            fullname=user.fullname,
            email=user.email,
            phone=user.phone,
            password=user.password,
            date_of_birth=payload.date_of_birth,
            gender=payload.gender,
            address=payload.address,
            reason=payload.reason,
        )
        return self.repository.add_patient(patient)

    def get_patient(self, patient_id: UUID) -> Patient:
        patient = self.repository.get_patient(patient_id)
        if patient is None:
            raise NotFoundError(f"Patient {patient_id} not found")
        return patient

    def list_patients(self) -> list[Patient]:
        return self.repository.list_patients()

    def update_patient(self, patient_id: UUID, payload: PatientUpdate) -> Patient:
        patient = self.get_patient(patient_id)
        email = payload.email
        if email is not None and payload.email != patient.email:
            if self.user_repository.get_user_by_email(email):
                raise ConflictError(f"An account with email '{payload.email}' already exists")

        data = payload.model_dump(exclude_unset=True)
        updated = self.repository.update_patient(patient_id, data)
        if updated is None:
            raise NotFoundError(f"Patient {patient_id} not found")
        return updated

    def delete_patient(self, patient_id: UUID) -> None:
        self.get_patient(patient_id)
        self.repository.delete_patient(patient_id)