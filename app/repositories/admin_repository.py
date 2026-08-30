from uuid import UUID
from models.admin import Admin
from repositories.in_memory_repository import InMemoryRepository


class AdminRepository(InMemoryRepository[Admin]):
    pass
    # def find_by_id(self, admin_id: UUID) -> Admin | None:
    #     return self.get_by_id(admin_id)