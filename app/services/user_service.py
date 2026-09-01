from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.models.user_role import UserRole

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, user_data: UserCreate) -> User:
        existing_user = self.user_repository.find_by_email(user_data.email)

        if existing_user is not None:
            raise ValueError("User already exists")

        user = User(
            fullname=user_data.fullname,
            email=user_data.email,
            phone=user_data.phone,
            password=user_data.password,
            role=UserRole.PATIENT
        )

        return self.user_repository.create(user)

    def login(self, email: str, password: str):
        saved_user = self.user_repository.find_by_email(email)
        if saved_user is None:
            raise ValueError("email or password is invalid")

        if saved_user.password != password:
            raise ValueError("email or password is invalid")

        return True

    def logout(self, email: str):
        saved_user = self.user_repository.find_by_email(email)
        if saved_user is None:
            return ValueError("email or password is invalid")

        return False