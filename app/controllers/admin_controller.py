# app/controllers/admin_controller.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.services.admin_service import AdminService
from app.config.dependencies import get_admin_service
from app.schemas.admin_schema import AdminCreate, AdminRead, UserSummary, DeleteUserResponse

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("/", response_model=AdminRead, status_code=status.HTTP_201_CREATED)
def create_admin(data: AdminCreate, service: AdminService = Depends(get_admin_service)):
    try:
        return service.register(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/users", response_model=list[UserSummary])
def list_all_users(service: AdminService = Depends(get_admin_service)):
    return service.list_all_users()


@router.get("/patients/{patient_id}/appointments")
def view_patient_appointments(patient_id: UUID, service: AdminService = Depends(get_admin_service)):
    return service.view_patient_appointments(patient_id)

@router.delete("/users/{user_id}", response_model=DeleteUserResponse)
def delete_user(user_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        return service.delete_user(user_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))