from uuid import UUID

from app.models.admin import Admin
from app.models.user_role import UserRole
from app.repositories.admin_repository import AdminRepository
from app.repositories.user_repository import UserRepository


class MySQLAdminRepository(AdminRepository):

    def __init__(self, users: UserRepository):
        self.users = users

    def add_admin(self, admin: Admin) -> Admin:
        # The `users` row is created by AdminService.create_admin;
        # there is no admin-specific table to write to.
        return admin

    def get_admin(self, admin_id: UUID) -> Admin | None:
        user = self.users.get_user(admin_id)
        if user and user.role == UserRole.ADMIN:
            return Admin(**user.model_dump())
        return None

    def list_admins(self) -> list[Admin]:
        return [
            Admin(**user.model_dump())
            for user in self.users.list_users()
            if user.role == UserRole.ADMIN
        ]

    def update_admin(self, admin_id: UUID, data: dict) -> Admin | None:
        if not self.get_admin(admin_id):
            return None
        self.users.update_user(admin_id, data)
        return self.get_admin(admin_id)

    def delete_admin(self, admin_id: UUID) -> bool:
        if not self.get_admin(admin_id):
            return False
        return self.users.delete_user(admin_id)
