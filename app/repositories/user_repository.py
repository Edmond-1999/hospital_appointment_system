from uuid import UUID
from typing import Optional

from app.models.user import User
from sqlmodel import Session, select


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def find_by_id(self, user_id: UUID) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()

    def find_by_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

    def exists_by_email(self, email):
        return self.find_by_email(email) is not None

    def find_all(self) -> list[User]:
        statement = select(User)
        return list(self.session.exec(statement).all())

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()



