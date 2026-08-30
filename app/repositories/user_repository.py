from uuid import UUID
from app.models.user import User
from app.repositories.in_memory_repository import InMemoryRepository


class UserRepository(InMemoryRepository[User]):

    def find_by_email(self, email: str) -> User | None:
        for user in self._items.values():
            if user.email.lower() == email.strip().lower():
                return user

        return None

    def find_by_id(self, user_id: UUID) -> User | None:
        return self._items.get(user_id)
