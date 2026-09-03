from datetime import datetime
from typing import Optional
from uuid import UUID

from app.models.appointment import Appointment
from app.models.appointment_status import AppointmentStatus
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository, doctor_repository: DoctorRepository,
                 user_repository: UserRepository):
        self.appointment_repository = appointment_repository
        self.doctor_repository = doctor_repository
        self.user_repository = user_repository

    def create_appointment(self, patient_id: UUID, department: str, appointment_datetime: datetime,
                            description: str) -> Appointment:
        doctors = self.doctor_repository.find_by_specialty(department)

        for doctor in doctors:
            existing = self.appointment_repository.find_by_doctor_datetime(doctor.user_id, appointment_datetime)
            if existing is None:
                doctor_user = self.user_repository.find_by_id(doctor.user_id)
                new_appointment = Appointment(
                    patient_id = patient_id,
                    doctor_id = doctor.user_id,
                    doctor_name = doctor_user.fullname,
                    department = department,
                    description = description,
                    appointment_datetime = appointment_datetime,
                )
                return self.appointment_repository.create(new_appointment)

        raise ValueError("No doctor is available at this time")

    def get_patient_appointments(self, patient_id: UUID) -> list[Appointment]:
        return self.appointment_repository.find_by_patient_id(patient_id)

    def get_doctor_appointments(self, doctor_id: UUID) -> list[Appointment]:
        return self.appointment_repository.find_by_doctor_id(doctor_id)

    def get_all_appointments(self) -> list[Appointment]:
        return self.appointment_repository.find_all()

    def change_status(self, appointment_id: UUID, doctor_id: UUID, new_status: AppointmentStatus) -> Appointment:
        appointment = self.appointment_repository.find_by_id(appointment_id)
        if appointment is None:
            raise ValueError(f"No appointment with id {appointment_id}")
        if appointment.doctor_id != doctor_id:
            raise ValueError("This appointment does not belong to you")

        transitions = {
            AppointmentStatus.CONFIRMED: appointment.confirm,
            AppointmentStatus.COMPLETED: appointment.complete,
            AppointmentStatus.CANCELLED: appointment.cancel,
        }
        transition = transitions.get(new_status)
        if transition is None:
            raise ValueError(f"Cannot change status to {new_status}")
        transition()

        return self.appointment_repository.update(appointment)

    def cancel_appointment(self, appointment_id: UUID, patient_id: Optional[UUID] = None) -> Appointment:
        appointment = self.appointment_repository.find_by_id(appointment_id)
        if appointment is None:
            raise ValueError(f"No appointment with id {appointment_id}")
        if patient_id is not None and appointment.patient_id != patient_id:
            raise ValueError(f"You can't cancel an appointment with id {appointment_id}")

        appointment.cancel()
        return self.appointment_repository.update(appointment)
