from abc import ABC, abstractmethod
from uuid import UUID

from app.models.doctor import Doctor


class DoctorRepository(ABC):

    @abstractmethod
    def add_doctor(self, doctor: Doctor) -> Doctor:
        ...

    @abstractmethod
    def get_doctor(self, doctor_id: UUID) -> Doctor | None:
        ...

    @abstractmethod
    def list_doctors(self) -> list[Doctor]:
        ...

    @abstractmethod
    def update_doctor(self, doctor_id: UUID, data: dict) -> Doctor | None:
        ...

    @abstractmethod
    def delete_doctor(self, doctor_id: UUID) -> bool:
        ...