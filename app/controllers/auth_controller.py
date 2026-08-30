from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_auth_service
from app.schemas.auth_schema import LoginRequest
from app.schemas.user_schema import UserRead
from app.exceptions import AuthenticationError
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=UserRead)
def login(payload: LoginRequest, service: AuthService = Depends(get_auth_service)):
    try:
        return service.login(payload.email, payload.password)
    except AuthenticationError as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, str(exc)) from exc


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(service: AuthService = Depends(get_auth_service)):
    service.logout()