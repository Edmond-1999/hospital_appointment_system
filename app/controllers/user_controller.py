
from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_user_service
from app.schemas.user_schema import UserResponse, UserCreate, LoginResponse, LoginRequest, LogoutRequest, LogoutResponse
from app.services.user_service import UserService


router = APIRouter(prefix="/user", tags=["user"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    user = service.register(user_data)
    return user

@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginRequest, service : UserService = Depends(get_user_service)):
    try:
        is_authenticated = service.login(login_data.email, login_data.password)

        if is_authenticated:
            return LoginResponse(message = "login successful")

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.post("/logout")
def logout(logout_data: LogoutRequest, service : UserService = Depends(get_user_service)):

    try:
        return service.logout(logout_data.email)


    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

