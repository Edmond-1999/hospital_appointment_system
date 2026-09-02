from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from app.config.dependencies import get_patient_service
from app.services.patient_service import PatientService
from app.schemas.appointment_schema import BookAppointmentResponse, BookAppointmentRequest
from app.schemas.patient_schema import PatientCreate, PatientRead


router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def register_patient(data: PatientCreate, service: PatientService = Depends(get_patient_service)):
    try:
        return service.register(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.post("/{patient_id}/appointments", response_model=BookAppointmentResponse)
def book_appointment(patient_id: UUID, appointment_data: BookAppointmentRequest, service: PatientService = Depends(get_patient_service)):
    return service.book_appointment(patient_id, appointment_data.department_name, appointment_data.appointment_datetime, appointment_data.description,
    )

@router.get("/{patient_id}/appointments")
def view_appointments(patient_id: UUID, service: PatientService = Depends(get_patient_service)):
    return service.view_appointments(patient_id)

@router.delete("/{patient_id}/appointments/{appointment_id}")
def cancel_appointment(patient_id: UUID, appointment_id: UUID, service: PatientService = Depends(get_patient_service)):
    return service.cancel_appointment(patient_id, appointment_id)
