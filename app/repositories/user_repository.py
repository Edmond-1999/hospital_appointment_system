from abc import ABC, abstractmethod
from uuid import UUID

from app.models.user import User




class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        ...

    @abstractmethod
    def get_user(self, user_id: UUID) -> User | None:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        ...

    @abstractmethod
    def list_users(self) -> list[User]:
        ...

    @abstractmethod
    def update_user(self, user_id: UUID, data: dict) -> User | None:
        ...

    @abstractmethod
    def delete_user(self, user_id: UUID) -> bool:
        ...


