# from app.repositories.user_repository import UserRepository
# from app.schemas.user_schema import UserCreate
# from app.models.user_role import UserRole
# from app.models.patient import Patient
# from app.repositories.doctor_repository import DoctorRepository
# from app.repositories.patient_repository import PatientRepository
#
#
# class UserService:
#     def __init__(self, user_repository: UserRepository, doctor_repository: DoctorRepository, patient_repository: PatientRepository):
#         self.user_repository = user_repository
#         self.doctor_repository = doctor_repository
#         self.patient_repository = patient_repository
#
#
#     def register(self, user_data: UserCreate) -> Patient:
#         existing_user = self.user_repository.find_by_email(user_data.email)
#
#         if existing_user is not None:
#             raise ValueError("User already exists")
#
#         patient = Patient(
#             fullname=user_data.fullname,
#             email=user_data.email,
#             phone=user_data.phone,
#             password=user_data.password,
#             date_of_birth = user_data.date_of_birth,
#             gender = user_data.gender,
#             address = user_data.address,
#             role=UserRole.PATIENT
#         )
#
#         self.user_repository.create(patient)
#         self.patient_repository.create(patient)
#
#         return patient
#
#     def login(self, email: str, password: str):
#         saved_user = self.user_repository.find_by_email(email)
#         if saved_user is None:
#             raise ValueError("email or password is invalid")
#
#         if saved_user.password != password:
#             raise ValueError("email or password is invalid")
#
#         return True
#
#     def logout(self, email: str):
#         saved_user = self.user_repository.find_by_email(email)
#         if saved_user is None:
#             return ValueError("email or password is invalid")
#
#         return False