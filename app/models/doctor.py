from app.models.user import User


class Doctor(User):
    specialization: str
    department: str