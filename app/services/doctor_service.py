
from uuid import UUID

from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.patient_repository import PatientRepository
from app.models.patient import Patient
from app.models.enums import AppointmentStatus


class DoctorService:
    def __init__(self, doctor_repository: DoctorRepository, appointment_repository: AppointmentRepository, patient_repository: PatientRepository):
        self.doctor_repository = doctor_repository
        self.appointment_repository = appointment_repository
        self.patient_repository = patient_repository


    def view_appointments(self, doctor_id: UUID):
        return self.appointment_repository.find_by_doctor(doctor_id)

    def view_patients(self, doctor_id: UUID) -> list[Patient]:
        appointments = self.appointment_repository.find_by_doctor(doctor_id)

        patients = []

        for appointment in appointments:
            patient = self.patient_repository.get_by_id(appointment.patient_id)

            if patient is not None:
                patients.append(patient)

        return patients


    def change_status(self, doctor_id: UUID, appointment_id: UUID, status: AppointmentStatus):
        appointment = self.appointment_repository.get_by_id(appointment_id)

        if appointment is None:
            raise ValueError(f"Appointment with id {appointment_id} does not exist")

        if appointment.doctor_id != doctor_id:
            raise ValueError(f"You can't change status of appointment with id {appointment_id}")

        elif status == AppointmentStatus.CONFIRMED:
            appointment.confirm()

        elif status == AppointmentStatus.COMPLETED:
            appointment.complete()

        elif status == AppointmentStatus.CANCELLED:
            appointment.cancel()

        else:
            raise ValueError(f"Invalid appointment status {status}")


        self.appointment_repository.update(appointment_id, appointment)


