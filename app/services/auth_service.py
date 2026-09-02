from app.repositories.user_repository import UserRepository
from app.models.user import User

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if user is None or user.password != password:
            raise ValueError("email or password is invalid")
        return user

    def logout(self, email: str) -> bool:
        user = self.user_repository.find_by_email(email)
        if user is None:
            raise ValueError("email or password is invalid")
        return True