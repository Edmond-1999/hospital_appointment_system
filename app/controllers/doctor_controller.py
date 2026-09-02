from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session

from app.repositories.doctor_repository import DoctorRepository
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.doctor_schema import DoctorRead, DoctorCreate
from app.services.appointment_service import AppointmentService
from app.services.doctor_service import DoctorService
from app.config.dependencies import get_doctor_service

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CREATED)
def register(data: DoctorCreate, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.register(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{doctor_id}/appointments")
def view_appointments(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_appointments(doctor_id)


@router.patch("/{doctor_id}/appointments/{appointment_id}/status")
def change_status(appointment_id: UUID, appointment_status: str,service: DoctorService = Depends(get_doctor_service)):
    return service.change_status(appointment_id, appointment_status)