from abc import ABC, abstractmethod
from uuid import UUID

from app.models.admin import Admin


class AdminRepository(ABC):
    @abstractmethod
    def add_admin(self, admin: Admin) -> Admin: ...

    @abstractmethod
    def get_admin(self, admin_id: UUID) -> Admin | None: ...

    @abstractmethod
    def list_admins(self) -> list[Admin]: ...

    @abstractmethod
    def update_admin(self, admin_id: UUID, data: dict) -> Admin | None: ...

    @abstractmethod
    def delete_admin(self, admin_id: UUID) -> bool: ...
