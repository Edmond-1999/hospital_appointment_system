import pytest
import test_engine
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.testing.engines import testing_engine
from sqlmodel import SQLModel, Session


class TestAppointmentModel:

    @pytest.fixure
    def db_session(self):
        testengine = create_engine(
            "sqlite:///:memory:", connect_args={"check_same_thread": False},
            poolclass=StaticPool)

        SQLModel.metadata.create_all(test_engine)

        with Session(test_engine) as session:
            yield session

        SQLModel.metadata.drop_all(testengine)