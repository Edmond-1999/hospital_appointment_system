from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")

class InMemoryRepository(Generic[T]):
    def __init__(self):
        self._items: dict[UUID, T] = {}

    def create(self, item: T) -> T:
        self._items[item.id] = item
        return item

    def get_by_id(self, item_id: UUID) -> T | None:
            return self._items.get(item_id)

    def update(self, item_id: UUID, item: T) -> T:
        self._items[item_id] = item
        return item

    def delete(self, item_id: UUID) -> None:
        self._items.pop(item_id, None)