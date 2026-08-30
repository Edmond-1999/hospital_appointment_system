import datetime
from uuid import UUID

from models.doctor_availability import DoctorAvailability
from repositories.in_memory_repository import InMemoryRepository


class DoctorAvailabilityRepository(InMemoryRepository[DoctorAvailability]):
    def find_doctor_by_datetime(self, doctor_id: UUID, available_datetime: datetime) -> DoctorAvailability | None:
        for availability in self._items.values():

            if availability.doctor_id == doctor_id and availability.available_datetime == available_datetime:
                return availability

        return None