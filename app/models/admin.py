import datetime
from uuid import UUID

from app.models.user import User
from app.models.department import Department
from app.models.doctor import Doctor
from app.models.enums import AppointmentStatus


class Admin(User):

    def register_doctor(self, doctor: Doctor) -> Doctor:
        return self.doctor_repository.create(doctor)

    def reschedule_appointment(self, appointment_id: UUID, new_date: datetime) -> None:

        pass

    def create_department(self, department: Department) -> None :
        pass

    def cancel_appointment(self, appointment_id: UUID) -> None:
        pass

    def change_status(self, appointment_id: UUID, status: AppointmentStatus) -> None:
        pass
