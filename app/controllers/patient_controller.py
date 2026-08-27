from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, ConfigDict
from app.dependencies import get_patient_service
from app.models.patient import Patient
# from exceptions import ConflictError, NotFoundError
from app.services.patient_service import PatientService

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=Patient, status_code=status.HTTP_201_CREATED)
def register_patient(
        payload: Patient,
        service: PatientService = Depends(get_patient_service)
):
    return service.register_patient(payload)
    # try:
    #     return service.register_patient(payload)
    # except ConflictError as exc:
    #     raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/", response_model=list[Patient])
def list_patients(
    service: PatientService = Depends(get_patient_service)
):
    return service.list_patients()


@router.get("/{patient_id}", response_model=Patient)
def get_patient(patient_id: int, service: PatientService = Depends(get_patient_service)):
    return service.get_patient(patient_id)
    # try:
    #     return service.get_patient(patient_id)
    # except NotFoundError as exc:
    #     raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc


@router.patch("/{patient_id}", response_model=Patient)
def update_patient(
    patient_id: int, patient: Patient, service: PatientService = Depends(get_patient_service)
):
    return service.update_patient_profile(patient_id)
    # try:
    #     return service.update_patient_profile(patient_id)
    # except NotFoundError as exc:
    #     raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
    # except ConflictError as exc:
    #     raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/{patient_id}")
def delete_patient(
        patient_id: int,
        service: PatientService = Depends(get_patient_service)
):
    return service.delete_patient(patient_id)
    # try:
    #     service.delete_patient(patient_id)
    # except NotFoundError as exc:
    #     raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc