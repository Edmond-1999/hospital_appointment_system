from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_patient_service
from app.exceptions import ConflictError, NotFoundError
from app.schemas.patient_schema import PatientCreate, PatientRead, PatientUpdate
from app.services.patient_service import PatientService

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def create_patient(payload: PatientCreate, service: PatientService = Depends(get_patient_service)):
    try:
        return service.create_patient(payload)
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/", response_model=list[PatientRead])
def list_patients(service: PatientService = Depends(get_patient_service)):
    return service.list_patients()


@router.get("/{patient_id}", response_model=PatientRead)
def get_patient(patient_id: UUID, service: PatientService = Depends(get_patient_service)):
    try:
        return service.get_patient(patient_id)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc


@router.patch("/{patient_id}", response_model=PatientRead)
def update_patient(
    patient_id: UUID, payload: PatientUpdate, service: PatientService = Depends(get_patient_service)
):
    try:
        return service.update_patient(patient_id, payload)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: UUID, service: PatientService = Depends(get_patient_service)):
    try:
        service.delete_patient(patient_id)
    except NotFoundError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc