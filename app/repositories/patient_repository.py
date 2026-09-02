from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from app.models.patient import Patient


class PatientRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, patient: Patient) -> Patient:
        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return patient

    def find_by_id(
        self,
        user_id: UUID
    ) -> Optional[Patient]:
        statement = select(Patient).where(
            Patient.user_id == user_id
        )

        return self.session.exec(statement).first()


    def find_all(self) -> list[Patient]:
        statement = select(Patient)
        return list(self.session.exec(statement).all())

    def update(self, patient: Patient, updates: dict) -> Patient:
        for field, value in updates.items():
            setattr(patient, field, value)

        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return patient

    def delete(self, patient: Patient) -> None:
        self.session.delete(patient)
        self.session.commit()
