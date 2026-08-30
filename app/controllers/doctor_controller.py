from uuid import UUID

from fastapi import APIRouter, Depends

from app.schemas.appointment_schema import UpdateAppointmentStatusRequest
from app.services.doctor_service import DoctorService
from app.dependencies import get_doctor_service

router = APIRouter(prefix="/doctors", tags=["Doctors"])
@router.get("/{doctor_id}/appointments")
def view_appointments(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_appointments(doctor_id)


@router.get("/{doctor_id}/patients")
def view_patients(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_patients(doctor_id)

@router.patch("/{doctor_id}/appointments/{appointment_id}/status")
def change_appointment_status(doctor_id: UUID, appointment_id: UUID,
                              payload: UpdateAppointmentStatusRequest,
                              service: DoctorService = Depends(get_doctor_service)):

    return service.change_status(doctor_id, appointment_id, payload.status)