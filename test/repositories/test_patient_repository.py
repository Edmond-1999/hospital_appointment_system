import pytest
from datetime import date
from uuid import uuid4
from sqlmodel import SQLModel, create_engine, Session

from app.models.user import User
from app.models.patient import Patient
from app.models.user_role import UserRole
from app.repositories.patient_repository import PatientRepository

test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False}
)


class TestPatientRepository:
    @pytest.fixture
    def session(self):
        SQLModel.metadata.create_all(test_engine)
        with Session(test_engine) as session:
            yield session
        SQLModel.metadata.drop_all(test_engine)

    @pytest.fixture
    def saved_user(self, session) -> User:
        user = User(
            fullname="Janeth John",
            email="janeth@gmail.com",
            phone="1234567890",
            password="password123",
            role=UserRole.PATIENT,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @pytest.fixture
    def saved_patient(self, session, saved_user) -> Patient:
        patient = Patient(
            user_id=saved_user.id,
            date_of_birth=date(2002, 1, 1),
            gender="female",
            address="123 Sabo Street",
        )
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient

    def test_create(self, session, saved_user):
        repo = PatientRepository(session)
        patient = Patient(
            user_id=saved_user.id,
            date_of_birth=date(2002, 1, 1),
            gender="female",
            address="123 Sabo Street",
        )

        created_patient = repo.create(patient)

        assert created_patient.user_id == saved_user.id
        assert created_patient.gender == "female"
        assert created_patient.address == "123 Sabo Street"

    def test_find_by_id(self, session, saved_patient):
        repo = PatientRepository(session)

        found_patient = repo.find_by_id(saved_patient.user_id)

        assert found_patient is not None
        assert found_patient.user_id == saved_patient.user_id
        assert found_patient.gender == "female"

    def test_find_by_id_returns_none_when_missing(self, session):
        repo = PatientRepository(session)

        found_patient = repo.find_by_id(uuid4())

        assert found_patient is None

    def test_find_all(self, session, saved_patient):
        repo = PatientRepository(session)

        patients = repo.find_all()

        assert len(patients) == 1
        assert patients[0].user_id == saved_patient.user_id

    def test_update(self, session, saved_patient):
        repo = PatientRepository(session)

        updated_patient = repo.update(saved_patient, {"address": "22 New Street"})

        assert updated_patient.address == "22 New Street"

    def test_delete(self, session, saved_patient):
        repo = PatientRepository(session)

        repo.delete(saved_patient)

        assert repo.find_by_id(saved_patient.user_id) is None