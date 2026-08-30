from uuid import UUID

from fastapi import APIRouter, Depends

from app.services.patient_service import PatientService
from app.dependencies import get_patient_service
from app.schemas.appointment_schema import BookAppointmentResponse, BookAppointmentRequest

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/{patient_id}/appointments")
def view_appointments(patient_id: UUID, service: PatientService = Depends(get_patient_service)):
    return service.view_appointments(patient_id)


@router.post("/{patient_id}/appointments", response_model=BookAppointmentResponse)
def book_appointment(patient_id: UUID, appointment_data: BookAppointmentRequest,  service: PatientService = Depends(get_patient_service)):

    return service.book_appointment(patient_id, appointment_data.department_id, appointment_data.appointment_datetime)
