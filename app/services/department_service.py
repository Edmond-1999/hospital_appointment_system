from repositories.department_repository import DepartmentRepository


class DepartmentService:
    def __init__(self, department_repository: DepartmentRepository):
        self.department_repository = department_repository

