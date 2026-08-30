

from app.models.department import Department
from app.repositories.in_memory_repository import InMemoryRepository
from models.doctor import Doctor

class DepartmentRepository(InMemoryRepository[Department]):
    def find_by_department_id(self, department_id: int) -> list[Doctor]:
        doctors = []

        for doctor in self._items.values():
            if doctor.deparment_id == department_id:
                doctors.append(doctor)

        return doctors