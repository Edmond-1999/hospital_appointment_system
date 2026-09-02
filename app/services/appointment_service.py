from datetime import datetime
from uuid import UUID

from app.models.appointment import Appointment
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.doctor_repository import DoctorRepository


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository, doctor_repository: DoctorRepository):
        self.appointment_repository = appointment_repository
        self.doctor_repository = doctor_repository

    def create_appointment(self, patient_id: UUID, department: str, appointment_datetime: datetime,
                           description: str) -> Appointment:
        doctors = self.doctor_repository.find_by_id(department)

        for doctor in doctors:
            appointment = self.appointment_repository.find_doctor_by_datetime(doctor.id, appointment_datetime)
            if appointment is None:
                new_appointment = Appointment(patient_id=patient_id,
                                              doctor_id=doctor.id,
                                              department_id=department,
                                              appointment_datetime=appointment_datetime,
                                              description=description)

                return self.appointment_repository.create(new_appointment)

        raise ValueError("No doctor is available at this time")

    def get_appointments_status(self, patient_id: UUID) -> list[Appointment]:
        return self.appointment_repository.find_by_patient(patient_id)

    def cancel_appointment(self, appointment_id: UUID, user_id: UUID) -> None:
        appointment = self.appointment_repository.get_by_id(appointment_id)

        if appointment is None:
            raise ValueError(f"No appointment with id {appointment_id}")
        if appointment.patient_id != user_id:
            raise ValueError(f"You can't cancel an appointment with id {appointment_id}")

        appointment.cancel()

        self.appointment_repository.update(appointment_id, appointment)



    
    
    
    