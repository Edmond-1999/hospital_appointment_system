from abc import ABC, abstractmethod
from uuid import UUID

from app.models.patient import Patient

class PatientRepository(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient) -> Patient: ...

    @abstractmethod
    def get_patient(self, patient_id: UUID) -> Patient | None: ...

    @abstractmethod
    def list_patients(self) -> list[Patient]: ...

    @abstractmethod
    def update_patient(self, patient_id: UUID, data: dict) -> Patient | None: ...

    @abstractmethod
    def delete_patient(self, patient_id: UUID) -> bool: ...

