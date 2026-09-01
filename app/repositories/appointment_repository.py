from sqlmodel import Session


class AppointmentRepository:
    def __init__(self, session: Session):
        self.session = session