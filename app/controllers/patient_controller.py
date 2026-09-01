from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.repositories.appointment_repository import AppointmentRepository
from app.services.appointment_service import AppointmentService
from app.services.patient_service import PatientService
from app.config.dependencies import get_session
from app.schemas.appointment_schema import BookAppointmentResponse, BookAppointmentRequest


router = APIRouter(prefix="/patients", tags=["patients"])

def get_patient_service(session: Session = Depends(get_session)):
    appointment_repository = AppointmentRepository(session)
    appointment_service = AppointmentService(appointment_repository)
    return PatientService(appointment_service)

@router.get("/{patient_id}/appointments")
def view_appointments(patient_id: UUID, service: PatientService = Depends(get_patient_service)):
    return service.view_appointments(patient_id)


@router.post("/{patient_id}/appointments", response_model=BookAppointmentResponse)
def book_appointment(patient_id: UUID, appointment_data: BookAppointmentRequest,  service: PatientService = Depends(get_patient_service)):

    return service.book_appointment(patient_id, appointment_data.department_id, appointment_data.appointment_datetime)