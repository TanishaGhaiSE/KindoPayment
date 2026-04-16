# app/repositories/registration_repository.py

from typing import Optional
from sqlmodel import Session, select

from app.models.registrations import Registrations
from app.repositories.interfaces import RegistrationRepository as RegistrationRepositoryInterface


class RegistrationRepository(RegistrationRepositoryInterface):

    def get(self, session: Session, reg_id: int) -> Optional[Registrations]:
        return session.get(Registrations, reg_id)

    def find_by_trip_student(
        self, session: Session, trip_id: int, student_id: int
    ) -> Optional[Registrations]:
        return session.exec(
            select(Registrations).where(
                Registrations.trip_id == trip_id,
                Registrations.student_id == student_id,
            )
        ).first()

    def create(self, session: Session, reg: Registrations) -> Registrations:
        session.add(reg)
        session.commit()
        session.refresh(reg)
        return reg