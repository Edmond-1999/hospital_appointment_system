from typing import Optional
from uuid import UUID

from sqlmodel import Session, select

from app.models.admin import Admin


class AdminRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, admin: Admin) -> Admin:
        self.session.add(admin)
        self.session.commit()
        self.session.refresh(admin)
        return admin

    def find_by_id(self, user_id: UUID) -> Optional[Admin]:
        statement = select(Admin).where(Admin.user_id == user_id)
        return self.session.exec(statement).first()

    def find_all(self) -> list[Admin]:
        return list(self.session.exec(select(Admin)).all())

    def update(self, admin: Admin, updates: dict) -> Admin:
        for field, value in updates.items():
            setattr(admin, field, value)
        self.session.add(admin)
        self.session.commit()
        self.session.refresh(admin)
        return admin

    def delete(self, admin: Admin) -> None:
        self.session.delete(admin)
        self.session.commit()