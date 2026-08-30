from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_admin_service
from app.exceptions import ConflictError, NotFoundError
from app.schemas.admin_schema import AdminCreate, AdminRead, AdminUpdate
from app.services.admin_service import AdminService

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("/", response_model=AdminRead, status_code=status.HTTP_201_CREATED)
def create_admin(payload: AdminCreate, service: AdminService = Depends(get_admin_service)):
    try:
        return service.create_admin(payload)
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/", response_model=list[AdminRead])
def list_admins(service: AdminService = Depends(get_admin_service)):
    return service.list_admins()


@router.get("/{admin_id}", response_model=AdminRead)
def get_admin(admin_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        return service.get_admin(admin_id)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc


@router.patch("/{admin_id}", response_model=AdminRead)
def update_admin(
    admin_id: UUID, payload: AdminUpdate, service: AdminService = Depends(get_admin_service)
):
    try:
        return service.update_admin(admin_id, payload)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_admin(admin_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        service.delete_admin(admin_id)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
