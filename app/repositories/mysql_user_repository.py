from uuid import UUID

from app.database import get_connection
from app.repositories.user_repository import UserRepository

from app.models.user import User


class MysqlUserRepository(UserRepository):
    @staticmethod
    def _row_to_model(row: dict) -> User:
        return User(
            id=row['id'],
            fullname=row["fullname"],
            email=row["email"],
            phone=row["phone"],
            password=row["password"],
            role=row["role"],
        )

    def add_user(self, user: User) -> User:
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute(
                """INSERT INTO users (id, fullname, email, phone, password, role)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                (str(user.id), user.fullname, user.email, user.phone, user.password, user.role.value),
            )
            db.commit()
        return user

    def get_user(self, user_id: UUID) -> User | None:
        with get_connection() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (str(user_id),))
            row = cursor.fetchone()
        return self._row_to_model(row) if row else None

    def get_user_by_email(self, email: str) -> User | None:
        with get_connection() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s", (str(email),))
            row = cursor.fetchone()
        return self._row_to_model(row) if row else None

    def list_users(self) -> list[User]:
        with get_connection() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users ORDER BY id")
            rows = cursor.fetchall()
        return [self._row_to_model(row) for row in rows]

    def update_user(self, user_id: UUID, data: dict) -> User | None:
        allowed = ("fullname", "email", "phone", "password")
        changes = {key: value for key, value in data.items() if key in allowed}
        if not changes:
            return self.get_user(user_id)

        values = [changes[key] for key in changes]
        values.append(str("user_id"))
        sql = ", ".join(f"{key} = %s" for key in changes)

        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE users SET {sql} WHERE id = %s", values)
            db.commit()
        return self.get_user(user_id)

    def delete_user(self, user_id: UUID) -> bool:
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (str(user_id),))
            deleted = cursor.rowcount > 0
            db.commit()
        return deleted