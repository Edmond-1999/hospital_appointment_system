from uuid import UUID

from models.patient import Patient
from repositories.in_memory_repository import InMemoryRepository


class PatientRepository(InMemoryRepository[Patient]):
    pass

    # def find_by_id(self, patient_id: UUID) -> Patient | None:
    #     return self._items.get(patient_id)
    #
    # def save(self, patient: Patient) -> Patient:
    #     pass