from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

user_repository = UserRepository()

def get_user_service() -> UserService:
    return UserService(user_repository)