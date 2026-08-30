from uuid import UUID
from app.models.doctor import Doctor
from app.repositories.in_memory_repository import InMemoryRepository


class DoctorRepository(InMemoryRepository[Doctor]):
    def find_by_department(self, department_id: UUID) -> list[Doctor]:
        doctors = []

        for doctor in self._items.values():
            if doctor.department_id == department_id:
                doctors.append(doctor)

        return doctors




