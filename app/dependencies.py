from fastapi import Depends

from app.repositories.user_repository import UserRepository
from app.repositories.mysql_user_repository import MysqlUserRepository
from app.repositories.patient_repository import PatientRepository
from app.repositories.mysql_patient_repository import MySQLPatientRepository

from app.services.auth_service import AuthService
from app.services.patient_service import PatientService

_users = MysqlUserRepository()
_patients = MySQLPatientRepository(_users)

def get_user_repository() -> UserRepository:
    return _users

def get_patient_repository() -> PatientRepository:
    return _patients

def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository)

def get_patient_service(
        repository: PatientRepository = Depends(get_patient_repository),
        user_repository: UserRepository = Depends(get_user_repository),
) -> PatientService:
    return PatientService(repository, user_repository)
