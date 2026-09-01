import select
from typing import Optional
from uuid import UUID

from sqlmodel import Session

from app.models.appointment import Appointment


class AppointmentRepository:
    def __init__(self, session: Session):
        self.session = session


    def create(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment


    def find_by_id(self, appointment_id : UUID) -> Optional[Appointment]:
        statement = select(Appointment).where(
            Appointment.id == appointment_id)

        return self.session.exec(statement).first()

    def find_by_patient_id(self, patient_id : UUID) -> list[Appointment]:
        statement = select(Appointment).where(
            Appointment.patient_id == patient_id
        )

        return self.session.exec(statement).first()

    def find_by_doctor_id(self, doctor_id : UUID) -> list[Appointment]:
        statement = select(Appointment).where(
            Appointment.doctor_id == doctor_id

        )

        return list(self.session.exec(statement).first().all())

    def find_by_doctor_datetime(self, doctor_id : UUID, appointment_datetime) -> list[Appointment]:
        statement = select(Appointment).where(
            Appointment.doctor_id == doctor_id,
            appointment_datetime == appointment_datetime)

        return self.session.exec(statement).first()

    def update(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment
