import uuid
from datetime import datetime

import pytest
from sqlalchemy import StaticPool
from sqlmodel import SQLModel, Session, create_engine

from app.models.appointment import Appointment
from app.models.appointment_status import AppointmentStatus


class TestAppointmentModel:

    @pytest.fixture
    def db_session(self):
        test_engine = create_engine(
            "sqlite:///:memory:",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )

        SQLModel.metadata.create_all(test_engine)

        with Session(test_engine) as session:
            yield session

        SQLModel.metadata.drop_all(test_engine)

    def create_test_appointment(self, db_session: Session):
        appointment = Appointment(
            patient_id=uuid.uuid4(),
            doctor_id=uuid.uuid4(),
            doctor_name="Dr. Kenny",
            department="Cardiology",
            description="Normal check-up",
            appointment_datetime=datetime.now()
        )

        db_session.add(appointment)
        db_session.commit()
        db_session.refresh(appointment)

        return appointment

    def test_appointment_model_functions_properly( self, db_session: Session ):
        appointment = self.create_test_appointment(db_session)

        saved_appointment = db_session.get(
            Appointment,
            appointment.id
        )

        assert saved_appointment is not None
        assert saved_appointment.patient_id == appointment.patient_id
        assert saved_appointment.doctor_id == appointment.doctor_id
        assert saved_appointment.department == appointment.department
        assert saved_appointment.description == appointment.description
        assert saved_appointment.status == AppointmentStatus.PENDING

    def test_confirm_appointment(self, db_session: Session):
        appointment = self.create_test_appointment(db_session)

        appointment.confirm()

        db_session.add(appointment)
        db_session.commit()
        db_session.refresh(appointment)

        assert appointment.status == AppointmentStatus.CONFIRMED

    def test_complete_appointment(self, db_session: Session):
        appointment = self.create_test_appointment(db_session)

        appointment.complete()

        db_session.add(appointment)
        db_session.commit()
        db_session.refresh(appointment)

        assert appointment.status == AppointmentStatus.COMPLETED

    def test_cancel_appointment(self, db_session: Session):
        appointment = self.create_test_appointment(db_session)

        appointment.cancel()

        db_session.add(appointment)
        db_session.commit()
        db_session.refresh(appointment)

        assert appointment.status == AppointmentStatus.CANCELLED