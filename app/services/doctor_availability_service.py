from datetime import datetime
from uuid import UUID

from models.doctor_availability import DoctorAvailability
from repositories.doctor_availability_repository import DoctorAvailabilityRepository


class DoctorAvailabilityService:
    def __init__(self, doctor_availability_repository: DoctorAvailabilityRepository):
        self._doctor_availability_repository = doctor_availability_repository

    def check_doctor_availability(self, doctor_id: UUID, available_datetime: datetime) -> bool:
        availability = (self._doctor_availability_repository.find_doctor_by_datetime(doctor_id, available_datetime))

        return availability is None