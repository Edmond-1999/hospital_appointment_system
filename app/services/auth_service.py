from app.exceptions import AuthenticationError
from app.models.user import User
from app.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def login(self, email: str, password: str) -> User:
        user = self.repository.get_user_by_email(email)
        if user is None or user.password != password:
            raise AuthenticationError("Invalid email or password")
        return user

    @staticmethod
    def logout() -> None:
        return None
