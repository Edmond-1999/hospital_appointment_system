from uuid import UUID
from app.models.patient import Patient
from app.models.user_role import UserRole
from app.repositories.patient_repository import PatientRepository
from app.repositories.user_repository import UserRepository

from app.database import get_connection


class MySQLPatientRepository(PatientRepository):
    def __init__(self, users: UserRepository):
        self.users = users

    @staticmethod
    def _get_details(patient_id: UUID) -> dict | None:
        with get_connection() as db:
            cur = db.cursor(dictionary=True)
            cur.execute("SELECT * FROM patients WHERE id = %s", (str(patient_id),))
            return cur.fetchone()

    def _build(self, patient_id: UUID) -> Patient | None:
        user = self.users.get_user(patient_id)
        details = self._get_details(patient_id)
        if not user or user.role != UserRole.PATIENT or not details:
            return None
        return Patient(
            id=user.id,
            fullname=user.fullname,
            email=user.email,
            phone=user.phone,
            password=user.password,
            role=UserRole.PATIENT,
            date_of_birth=details["date_of_birth"],
            gender=details["gender"],
            address=details["address"],
            reason=details["reason"],
        )

    def add_patient(self, patient: Patient) -> Patient:
        with get_connection() as db:
            cur = db.cursor()
            cur.execute(
                """INSERT INTO patients (id, date_of_birth, gender, address, reason)
                   VALUES (%s, %s, %s, %s, %s)""",
                (str(patient.id), patient.date_of_birth, patient.gender,
                 patient.address, patient.reason),
            )
            db.commit()
        return patient

    def get_patient(self, patient_id: UUID) -> Patient | None:
        return self._build(patient_id)

    def list_patients(self) -> list[Patient | None]:
        with get_connection() as db:
            cur = db.cursor()
            cur.execute("SELECT id FROM patients ORDER BY id")
            ids = [UUID(row[0]) for row in cur.fetchall()]
        return [patient for patient in (self._build(index) for index in ids) if patient]

    def update_patient(self, patient_id: UUID, data: dict) -> Patient | None:
        patient = self.get_patient(patient_id)
        if not patient:
            return None

        user_data = {k: v for k, v in data.items()
                     if k in {"fullname", "email", "phone", "hashed_password"}}
        detail_data = {k: v for k, v in data.items()
                       if k in {"date_of_birth", "gender", "address", "reason"}}

        if user_data:
            self.users.update_user(patient_id, user_data)

        if detail_data:
            values = [v for v in detail_data.values()]
            values.append(str(patient_id))
            sql = ", ".join(f"{k} = %s" for k in detail_data)
            with get_connection() as db:
                cur = db.cursor()
                cur.execute(f"UPDATE patients SET {sql} WHERE id = %s", values)
                db.commit()

        return self.get_patient(patient_id)

    def delete_patient(self, patient_id: UUID) -> bool:
        deleted_user = self.users.delete_user(patient_id)
        with get_connection() as db:
            cur = db.cursor()
            cur.execute(f"DELETE FROM patients WHERE id = %s", (str(patient_id,)))
            db.commit()
        return deleted_user