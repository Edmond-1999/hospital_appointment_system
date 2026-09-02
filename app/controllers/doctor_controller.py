from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.repositories.appointment_repository import AppointmentRepository
from app.services.appointment_service import AppointmentService
from app.services.doctor_service import DoctorService
from app.config.dependencies import get_session


router = APIRouter(prefix="/doctors", tags=["doctors"])


def get_doctor_service(session: Session = Depends(get_session)):
    appointment_repository = AppointmentRepository(session)
    appointment_service = AppointmentService(appointment_repository)
    return DoctorService(appointment_service)


@router.get("/{doctor_id}/appointments")
def view_appointments(doctor_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_appointments(doctor_id)


@router.get("/{doctor_id}/patients/{patient_id}")
def view_patient(doctor_id: UUID, patient_id: UUID, service: DoctorService = Depends(get_doctor_service)):
    return service.view_patient(patient_id)


@router.patch("/{doctor_id}/appointments/{appointment_id}/status")
def change_status(doctor_id: UUID, appointment_id: UUID,status: str,service: DoctorService = Depends(get_doctor_service)):
    return service.change_status(appointment_id,status)