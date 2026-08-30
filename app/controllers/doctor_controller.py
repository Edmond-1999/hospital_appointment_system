from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_doctor_service
from app.exceptions import ConflictError, NotFoundError
from app.schemas.doctor_schema import DoctorRead, DoctorCreate, DoctorUpdate
from app.services.doctor_service import DoctorService

router = APIRouter(prefix = "/doctors", tags = ["Doctors"])

@router.post("/", response_model = DoctorRead, status_code = status.HTTP_201_CREATED)
def create_doctor(payload: DoctorCreate, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.create_doctor(payload)

    except ConflictError as exc:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = str(exc))from exc

@router.get("/", response_model = list[DoctorRead])
def list_doctors(service: DoctorService = Depends(get_doctor_service)):
    return service.list_doctors()

@router.get("/{doctor_id}", response_model = DoctorRead)
def get_doctor(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.get_doctor(doctor_id)

    except NotFoundError as exc:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(exc))from exc

@router.patch("/{doctor_id}", response_model = DoctorRead)
def update_doctor(doctor_id: UUID, payload: DoctorUpdate, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.update_doctor(doctor_id, payload)
    except NotFoundError as exc:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(exc))from exc
    except ConflictError as exc:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = str(exc))from exc

@router.delete("/{doctor_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.delete_doctor(doctor_id)
    except NotFoundError as exc:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(exc)) from exc