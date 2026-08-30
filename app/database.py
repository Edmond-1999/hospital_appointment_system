# import mysql.connector
#
# connection = mysql.connector.connect(
#     host=os.getenv("DB_HOST", "localhost"),
#     port=int(os.getenv("DB_PORT", "3306")),
#     user=os.getenv("DB_USER", "root"),
#     password=os.getenv("DB_PASSWORD", ""),
#     database=os.getenv("DB_NAME", "hospital_appointment"),
# )

import os

from contextlib import contextmanager
from typing import Any, Iterator

def settings() -> dict:
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "1234"),
        "database": os.getenv("DB_NAME", "hospital_appointment"),
    }

@contextmanager
def get_connection() -> Iterator[Any]:
    try:
        import mysql.connector
    except ImportError as exc:
        raise RuntimeError(
            "MySQL support not installed."
        )

    connection = mysql.connector.connect(**settings())
    try:
        yield connection
    finally:
        connection.close()

