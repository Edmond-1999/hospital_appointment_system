# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlmodel import Session
#
# from app.config.dependencies import get_session
# from app.repositories.user_repository import UserRepository
# from app.schemas.user_schema import UserResponse, UserCreate, LoginResponse, LoginRequest, LogoutRequest
# from app.services.user_service import UserService
# from app.repositories.patient_repository import PatientRepository
# from app.repositories.doctor_repository import DoctorRepository
#
# router = APIRouter(prefix="/user", tags=["user"])
#
# def get_user_service(session: Session = Depends(get_session)) -> UserService:
#     user_repository = UserRepository(session)
#     patient_repository = PatientRepository(session)
#     doctor_repository = DoctorRepository(session)
#     return UserService(user_repository, doctor_repository, patient_repository)
#
# @router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# def register(user_data: UserCreate, service: UserService = Depends(get_user_service)):
#     user = service.register(user_data)
#     return user
#
#
# @router.post("/login", response_model=LoginResponse)
# def login(login_data: LoginRequest, service : UserService = Depends(get_user_service)):
#     try:
#         is_authenticated = service.login(login_data.email, login_data.password)
#
#         if is_authenticated:
#             return LoginResponse(message = "login successful")
#
#     except ValueError as error:
#         raise HTTPException(status_code=404, detail=str(error))
#
# @router.post("/logout")
# def logout(logout_data: LogoutRequest, service : UserService = Depends(get_user_service)):
#
#     try:
#         return service.logout(logout_data.email)
#
#
#     except ValueError as error:
#         raise HTTPException(status_code=404, detail=str(error))