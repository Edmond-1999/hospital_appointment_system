from typing import Optional
from app.models.patient import Patient
from app.repositories.patient_repository import PatientRepository


class PatientNotFoundError(Exception):
    pass

class DuplicateEmailError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass



class PatientService:

    def __init__(self, repository: PatientRepository):
        self._repository = repository

    # ---------- registration / lookup ----------
    def register_patient(
        self,
        fullname: str,
        email: str,
        phone: str,
        password: str,
        date_of_birth: str,
        gender: str,
        address: str,
        reason: str,
    ) -> Patient:
        if self._repository.get_by_email(email) is not None:
            raise DuplicateEmailError(f"A patient with email '{email}' already exists.")

        patient = Patient(
            fullname=fullname,
            email=email,
            phone=phone,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            reason=reason,
        )
        return self._repository.add_patient(patient)

    def get_patient(self, patient_id: int) -> Patient:
        patient = self._repository.get_patient(patient_id)
        if patient is None:
            raise PatientNotFoundError(f"No patient found with id {patient_id}")
        return patient

    def list_patients(self) -> list[Patient]:
        return self._repository.list_patients()

    # ---------- mutation ----------
    def update_patient_profile(self, patient_id: int, **fields) -> Patient:
        patient = self.get_patient(patient_id)
        patient.update_profile(**fields)
        return self._repository.update(patient)

    def delete_patient(self, patient_id: int) -> None:
        if not self._repository.delete(patient_id):
            raise PatientNotFoundError(f"No patient found with id {patient_id}")

    # ---------- appointments ----------
    def book_appointment(self, patient_id: int, appointment) -> Patient:
        patient = self.get_patient(patient_id)
        patient.book_appointment(appointment)
        return self._repository.update(patient)

    def view_appointments(self, patient_id: int) -> list:
        patient = self.get_patient(patient_id)
        return patient.view_appointments()

    def cancel_appointment(self, patient_id: int, appointment_id: int) -> Patient:
        patient = self.get_patient(patient_id)
        patient.cancel_appointment(appointment_id)
        return self._repository.update(patient)

    # ---------- auth ----------
    def authenticate(self, email: str, password: str) -> Patient:
        patient = self._repository.get_by_email(email)
        if patient is None or not patient.login(password):
            raise InvalidCredentialsError("Invalid email or password.")
        return patient