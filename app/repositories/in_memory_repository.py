# from app.models.patient import Patient
# from app.repositories.patient_repository import PatientRepository
# from typing import List, Optional
#
# class InMemoryPatientRepository(PatientRepository):
#
#     def __init__(self):
#         self.patients: List[Patient] = []
#         self._next_id = 1
#
#     def add_patient(self, patient: Patient) -> Patient:
#         patient.id = self._next_id
#         self._next_id += 1
#
#         self.patients.append(patient)
#         return patient
#
#     def get_patient(self, patient_id: int) -> Optional[Patient]:
#         for patient in self.patients:
#             if patient.id == patient_id:
#                 return patient
#         return None
#
#     def get_by_email(self, email: str) -> Optional[Patient]:
#         for patient in self.patients:
#             if patient.email == email:
#                 return patient
#         return None
#
#     def list_patients(self) -> List[Patient]:
#         return self.patients
#
#     def update(self, patient_id: int, data: dict) -> Patient:
#         patient = self.get_patient(patient_id)
#         if patient is None:
#             raise ValueError("Patient not found")
#
#         for key, value in data.items():
#             setattr(patient, key, value)
#
#         return patient
#
#     def delete(self, patient_id: int) -> bool:
#         patient = self.get_patient(patient_id)
#
#         if patient is None:
#             return False
#
#         self.patients.remove(patient)
#         return True