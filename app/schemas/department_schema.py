from uuid import UUID

from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    name: str
    description: str


class DepartmentResponse(BaseModel):
    id: UUID
    name: str
    description: str