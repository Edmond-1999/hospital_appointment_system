from uuid import UUID, uuid4
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    # def __init__(self, _id: int, fullname: str, email: str, phone: str, password: str):
    id: UUID = Field(default_factory=uuid4)
    fullname = str
    email = str
    phone = str
    password = str

    def login(self, password: str) -> bool:
        return password == self.password

    def logout(self) -> None:
        print(f"{self.fullname} logged out.")

    def update_profile(self, **fields) -> None:
        for key, value in fields.items():
            if hasattr(self, key):
                setattr(self, key, value)


    def role(self) -> str:
        raise NotImplementedError

    def __repr__(self):
        return f"<{self.role()} id={self.id} name={self.fullname!r}>"