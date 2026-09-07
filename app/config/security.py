from uuid import UUID

from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from app.config.dependencies import get_session
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.models.user_role import UserRole


def require_admin(admin_id: UUID, session: Session = Depends(get_session)) -> User:
    user = UserRepository(session).find_by_id(admin_id)
    if user is None or not user.is_logged_in or user.role != UserRole.ADMIN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in as admin")
    return user


def require_patient_owner(patient_id: UUID, session: Session = Depends(get_session)) -> User:
    user = UserRepository(session).find_by_id(patient_id)
    if user is None or not user.is_logged_in:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")
    if user.role != UserRole.PATIENT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for this patient")
    return user


def require_doctor_owner(doctor_id: UUID, session: Session = Depends(get_session)) -> User:
    user = UserRepository(session).find_by_id(doctor_id)
    if user is None or not user.is_logged_in:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")
    if user.role != UserRole.DOCTOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for this doctor")
    return user