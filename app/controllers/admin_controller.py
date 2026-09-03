from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.appointment_schema import BookAppointmentResponse, AdminBookAppointmentRequest
from app.services.admin_service import AdminService
from app.config.dependencies import get_admin_service
from app.schemas.admin_schema import AdminCreate, AdminRead, UserSummary, DeleteUserResponse

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("/", response_model=AdminRead, status_code=status.HTTP_201_CREATED)
def register_admin(data: AdminCreate, service: AdminService = Depends(get_admin_service)):
    try:
        return service.register(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/users", response_model=list[UserSummary])
def list_all_users(service: AdminService = Depends(get_admin_service)):
    return service.list_all_users()


@router.delete("/users/{user_id}", response_model=DeleteUserResponse)
def delete_user(user_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        return service.delete_user(user_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.post("/appointments", response_model=BookAppointmentResponse, status_code=status.HTTP_201_CREATED)
def book_appointment_for_patient(data: AdminBookAppointmentRequest, service: AdminService = Depends(get_admin_service)):
    try:
        return service.book_appointment_for_patient(
            data.patient_id, data.department, data.appointment_datetime, data.description
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/appointments", response_model=list[BookAppointmentResponse])
def view_all_appointments(service: AdminService = Depends(get_admin_service)):
    return service.view_all_appointments()

@router.delete("/appointments/{appointment_id}", response_model=BookAppointmentResponse)
def cancel_appointment(appointment_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        return service.cancel_appointment(appointment_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))