from uuid import UUID

from sqlmodel import Session, select

from app.models.appointment import Appointment

class AppointmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment

    def find_by_id(self, appointment_id: UUID):
        statement = select(Appointment).where(Appointment.id == appointment_id)
        return self.session.exec(statement).first()

    def find_by_patient_id(self, patient_id: UUID):
        statement = select(Appointment).where(Appointment.patient_id == patient_id)
        return self.session.exec(statement).all()

    def find_by_doctor_id(self, doctor_id: UUID):
        statement = select(Appointment).where(Appointment.doctor_id == doctor_id)
        return self.session.exec(statement)

    def find_by_doctor_datetime(self, doctor_id: UUID, appointment_datetime):
        statement = select(Appointment).where(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_datetime == appointment_datetime,
        )
        return self.session.exec(statement).first()

    def update(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment