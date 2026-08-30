from fastapi import Depends

from app.repositories.doctor_repository import DoctorRepository
from app.repositories.mysql_doctor_repository import MySQLDoctorRepository
from app.repositories.user_repository import UserRepository
from app.repositories.mysql_user_repository import MysqlUserRepository
from app.repositories.patient_repository import PatientRepository
from app.repositories.mysql_patient_repository import MySQLPatientRepository
from app.repositories.admin_repository import AdminRepository
from app.repositories.mysql_admin_repository import MySQLAdminRepository

from app.services.auth_service import AuthService
from app.services.doctor_service import DoctorService
from app.services.patient_service import PatientService
from app.services.admin_service import AdminService


_users = MysqlUserRepository()
_patients = MySQLPatientRepository(_users)
_admins = MySQLAdminRepository(_users)
_doctors = MySQLDoctorRepository(_users)

def get_user_repository() -> UserRepository:
    return _users

def get_patient_repository() -> PatientRepository:
    return _patients

def get_admin_repository() -> AdminRepository:
    return _admins

def get_doctor_repository() -> DoctorRepository:
    return _doctors

def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository)

def get_patient_service(
        repository: PatientRepository = Depends(get_patient_repository),
        user_repository: UserRepository = Depends(get_user_repository),
) -> PatientService:
    return PatientService(repository, user_repository)

def get_admin_service(
    repository: AdminRepository = Depends(get_admin_repository),
    user_repository: UserRepository = Depends(get_user_repository),
) -> AdminService:
    return AdminService(repository, user_repository)


def get_doctor_service(
    repository: DoctorRepository = Depends(get_doctor_repository),
    user_repository: UserRepository = Depends(get_user_repository)
) -> DoctorService:

    return DoctorService(repository, user_repository)