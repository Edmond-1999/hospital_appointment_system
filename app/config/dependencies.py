from app.config.database import engine

from fastapi import Depends
from sqlmodel import Session

from app.repositories.user_repository import UserRepository
from app.repositories.patient_repository import PatientRepository
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.admin_repository import AdminRepository
from app.repositories.doctor_repository import DoctorRepository

from app.services.admin_service import AdminService
from app.services.auth_service import AuthService
from app.services.doctor_service import DoctorService
from app.services.patient_service import PatientService
from app.services.appointment_service import AppointmentService

def get_session():
    with Session(engine) as session:
        yield session

def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
    return AuthService(UserRepository(session))

def get_appointment_service(session: Session = Depends(get_session)) -> AppointmentService:
    appointment_repository = AppointmentRepository(session)
    doctor_repository = DoctorRepository(session)
    user_repository = UserRepository(session)
    return AppointmentService(appointment_repository, doctor_repository, user_repository)

def get_patient_service(
        session: Session = Depends(get_session),
        appointment_service: AppointmentService = Depends(get_appointment_service),
) -> PatientService:
    user_repository = UserRepository(session)
    patient_repository = PatientRepository(session)
    return PatientService(user_repository, patient_repository, appointment_service)

def get_doctor_service(
    session: Session = Depends(get_session),
    appointment_service: AppointmentService = Depends(get_appointment_service),
) -> DoctorService:
    return DoctorService(UserRepository(session), DoctorRepository(session), appointment_service)

def get_admin_service(
    session: Session = Depends(get_session),
    appointment_service: AppointmentService = Depends(get_appointment_service),
) -> AdminService:
    return AdminService(UserRepository(session), AdminRepository(session), PatientRepository(session), DoctorRepository(session), appointment_service)