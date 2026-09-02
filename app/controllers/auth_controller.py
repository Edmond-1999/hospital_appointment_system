from fastapi import APIRouter, Depends, HTTPException
from app.config.dependencies import get_auth_service
from app.services.auth_service import AuthService
from app.schemas.user_schema import LoginRequest, LoginResponse, LogoutRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, service: AuthService = Depends(get_auth_service)):
    try:
        user = service.login(data.email, data.password)
        return LoginResponse(message="login successful", role=user.role.value)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.post("/logout")
def logout(data: LogoutRequest, service: AuthService = Depends(get_auth_service)):
    try:
        service.logout(data.email)
        return {"message": "logout successful"}
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))