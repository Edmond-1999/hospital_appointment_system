from uuid import UUID, uuid4

from app.exceptions import ConflictError, NotFoundError
from app.models.admin import Admin
from app.models.user import User
from app.models.user_role import UserRole
from app.repositories.admin_repository import AdminRepository
from app.repositories.user_repository import UserRepository
from app.schemas.admin_schema import AdminCreate, AdminUpdate


class AdminService:
    def __init__(self, repository: AdminRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def create_admin(self, payload: AdminCreate) -> Admin:
        if self.user_repository.get_user_by_email(payload.email):
            raise ConflictError(f"An account with email '{payload.email}' already exists")

        user = User(
            id=uuid4(),
            fullname=payload.fullname,
            email=payload.email,
            phone=payload.phone,
            password=payload.password,
            role=UserRole.ADMIN,
        )
        self.user_repository.add_user(user)

        admin = Admin(
            id=user.id,
            fullname=user.fullname,
            email=user.email,
            phone=user.phone,
            password=user.password,
            role=UserRole.ADMIN,
        )
        return self.repository.add_admin(admin)

    def get_admin(self, admin_id: UUID) -> Admin:
        admin = self.repository.get_admin(admin_id)
        if admin is None:
            raise NotFoundError(f"Admin {admin_id} not found")
        return admin

    def list_admins(self) -> list[Admin]:
        return self.repository.list_admins()

    def update_admin(self, admin_id: UUID, payload: AdminUpdate) -> Admin:
        admin = self.get_admin(admin_id)
        email = payload.email
        if email is not None and payload.email != admin.email:
            if self.user_repository.get_user_by_email(email):
                raise ConflictError(f"An account with email '{email}' already exists")

        data = payload.model_dump(exclude_unset=True)
        updated = self.repository.update_admin(admin_id, data)
        if updated is None:
            raise NotFoundError(f"Admin {admin_id} not found")
        return updated

    def delete_admin(self, admin_id: UUID) -> None:
        self.get_admin(admin_id)
        self.repository.delete_admin(admin_id)
