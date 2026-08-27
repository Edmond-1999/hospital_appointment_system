from abc import ABC, abstractmethod
from app.models.patient import Patient
from typing import List

class PatientRepository(ABC):

    @abstractmethod
    def add_patient(self, patient: Patient) -> Patient:
       ...
    @abstractmethod
    def get_patient(self, patient_id: int) -> Patient | None:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Patient | None:
        ...

    @abstractmethod
    def list_patients(self, ) -> list[Patient]:
        ...

    @abstractmethod
    def update(self, patient_id: int, data: dict) -> Patient:
        ...

    @abstractmethod
    def delete(self, patient_id: int) -> bool:
        ...



