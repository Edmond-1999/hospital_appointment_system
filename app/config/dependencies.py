from sqlmodel import Session

from app.config.database import engine

def get_session():
    with Session(engine) as session:
        yield session


# from app.repositories.user_repository import UserRepository
# from app.services.user_service import UserService
# from app.repositories.doctor_repository import DoctorRepository
# from app.repositories.appointment_repository import AppointmentRepository
# from app.repositories.patient_repository import PatientRepository
# from app.services.doctor_service import DoctorService
# from app.services.appointment_service import AppointmentService
# from app.services.patient_service import PatientService
#
# user_repository = UserRepository()
# doctor_repository = DoctorRepository()
# appointment_repository = AppointmentRepository()
# patient_repository = PatientRepository()

# def get_user_service() -> UserService:
#     return UserService(user_repository)
#
# # def get_doctor_service() -> DoctorService:
# #     return DoctorService(doctor_repository, appointment_repository, patient_repository)
#
# def get_appointment_service() -> AppointmentService:
#     return AppointmentService(appointment_repository, doctor_repository)
#
# def get_patient_service() -> PatientService:
#     return PatientService(get_appointment_service())
