from typing import Optional
from uuid import UUID


from sqlmodel import Session, select

from app.models.doctor import Doctor


class DoctorRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, doctor: Doctor) -> Doctor:
        self.session.add(doctor)
        self.session.commit()
        self.session.refresh(doctor)
        return doctor

    # def save(self, doctor: Doctor) :
    #     self.session.add(doctor)
    #     self.session.commit()
    #     self.session.refresh(doctor)
    #     return doctor

    def find_by_id(self, doctor_id: UUID) -> Optional[Doctor]:
        statement = select(Doctor).where(Doctor.user_id == doctor_id)
        return self.session.exec(statement).first()

    # def find_by_email(self, email: str) -> Optional[Doctor]:
    #     statement = select(Doctor).where(Doctor.email == email)
    #     return self.session.exec(statement).first()

    def find_all(self) -> list[Doctor]:
        statement = select(Doctor)
        return list(self.session.exec(statement).all())

    # def exists_by_email(self, email: str) -> bool:
    #     return self.find_by_email(email) is not None

    def delete(self, doctor: Doctor) -> None:
        self.session.delete(doctor)
        self.session.commit()


    def find_by_specialty(self, specialty: str) -> list[Doctor]:
        statement = select(Doctor).where(Doctor.specialization == specialty)
        return list(self.session.exec(statement).all())


