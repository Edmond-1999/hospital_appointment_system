from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException

from app.schemas.appointment_schema import BookAppointmentResponse, ChangeAppointmentStatusRequest
from app.schemas.doctor_schema import DoctorRead, DoctorCreate
from app.services.doctor_service import DoctorService
from app.config.dependencies import get_doctor_service

router = APIRouter(prefix="/doctors", tags=["doctors"])

@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CREATED)
def register_doctor(data: DoctorCreate, service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.register(data)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{doctor_id}/appointments", response_model=list[BookAppointmentResponse])
def view_appointments(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_appointments(doctor_id)

@router.patch("/{doctor_id}/appointments/{appointment_id}/status", response_model=BookAppointmentResponse)
def change_status(doctor_id: UUID, appointment_id: UUID, data: ChangeAppointmentStatusRequest,
                   service: DoctorService = Depends(get_doctor_service)):
    try:
        return service.change_status(doctor_id, appointment_id, data.status)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))