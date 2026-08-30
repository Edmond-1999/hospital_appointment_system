from uuid import UUID

from app.database import get_connection
from app.models import user
from app.models.doctor import Doctor
from app.models.user_role import UserRole
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository


class MySQLDoctorRepository(DoctorRepository):
    def __init__(self, users: UserRepository):
        self.users = users

    @staticmethod
    def get_details(doctor_id: UUID) -> dict | None:
        with get_connection() as db:
            cur = db.cursor(dictionary=True)

            cur.execute("SELECT * FROM doctors WHERE doctor_id = %s", (str(doctor_id,),))

            return cur.fetchone()

    def _build(self, doctor_id: UUID) -> Doctor | None:
        user = self.users.get_user(doctor_id)
        details = self.get_details(doctor_id)
        if not user or not user.role != UserRole.DOCTOR or not details:
            return None

        return Doctor(
            id = user.id,
            fullname = user.fullname,
            email = user.email,
            phone = user.phone,
            password = user.password,
            role = UserRole.DOCTOR,
            specialization = details['specialization'],
            department_id = details['department_id']
        )

    def add_doctor(self, doctor: Doctor) -> Doctor:
        with get_connection() as db:
            cur = db.cursor()

            cur.execute("""INSERT INTO doctors 
            (id, specialization, department_id)
            VALUES (%s, %s, %s)
            """,
                (
                    str(doctor.id),
                    doctor.specialization,
                    str(doctor.department_id)
                    if doctor.department_id else None
                )
                        )

            db.commit()

        return doctor

    def get_doctor(self, doctor_id: UUID) -> Doctor | None:
        return self._build(doctor_id)

    def list_doctors(self) -> list[Doctor]:
        with get_connection() as db:
            cur = db.cursor()

            cur.execute("SELECT id FROM doctors ORDER BY id")

            doctor_ids = [
                UUID(row[0])
                for row in cur.fetchall()
            ]

            doctors = []

            for doctor_id in doctor_ids:
                doctor = self._build(doctor_id)

                if doctor:
                    doctors.append(doctor)

            return doctors


    def update_doctor(self, doctor_id: UUID, data : dict) -> Doctor | None:
        doctor = self.get_doctor(doctor_id)

        if not doctor:
            return None

        user_data = {
            key: value for key, value in data.items() if key in {
                "fullname",
                "email",
                "phone",
                "password"
            }
        }

        doctor_data = {
            key: value for key, value in data.items() if key in {
                "specialization",
                "department_id"
            }
        }

        if user_data:
            self.users.update_user(doctor_id, user_data)

        if doctor_data:

            values = []

            for value in doctor_data.values():
                if isinstance(value, UUID):
                    values.append(str(value))

                else:
                    values.append(value)

            values.append(str(doctor_id))

            sql = ", ".join(f"{key} = %s"
                    for key in doctor_data
                    )

            with get_connection() as db:
                cur = db.cursor()

                cur.execute(
                    f"""
                    UPDATE doctors
                    SET {sql}
                    WHERE id = %s
                    """, values
                )

                db.commit()

        return self.get_doctor(doctor_id)

    def delete_doctor(self, doctor_id: UUID) -> bool:

        deleted_user = self.users.delete_user(doctor_id)

        with get_connection() as db:
            cur = db.cursor()

            cur.execute(
                "DELETE FROM doctors WHERE id = %s",
                (str(doctor_id),)
            )
            db.commit()

        return deleted_user

