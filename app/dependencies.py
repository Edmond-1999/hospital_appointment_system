from fastapi import Depends

from app.repositories.patient_repository import PatientRepository
from app.repositories.in_memory_repository import InMemoryPatientRepository
from app.services.patient_service import PatientService


_repository = InMemoryPatientRepository()

def get_patient_repository() -> PatientRepository:
    return _repository

def get_patient_service(
        repository: PatientRepository = Depends(get_patient_repository),
) -> PatientService:
    return PatientService(repository)