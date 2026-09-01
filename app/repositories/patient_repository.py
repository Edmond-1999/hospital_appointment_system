from typing import Optional, List, Any, Sequence
from uuid import UUID

from sqlmodel import Session, select

from app.models.patient import Patient


class PatientRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, patient: Patient) -> Patient:
        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return patient

    def find_by_id(
        self,
        patient_id: UUID
    ) -> Optional[Patient]:
        statement = select(Patient).where(
            Patient.id == patient_id
        )

        return self.session.exec(statement).first()

    def find_by_email(
        self,
        email: str
    ) -> Optional[Patient]:
        statement = select(Patient).where(
            Patient.email == email
        )

        return self.session.exec(statement).first()

    def exists_by_email(self, email: str) -> bool:
        return self.find_by_email(email) is not None

    def list(self) -> Sequence[Any]:
        return self.session.exec(select(Patient)).all()