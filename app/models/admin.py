from app.models.user import User
from app.models.user_role import UserRole


class Admin(User):
    role: UserRole = UserRole.ADMIN
