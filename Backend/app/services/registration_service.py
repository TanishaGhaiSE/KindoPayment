# app/services/registration_service.py

from sqlmodel import Session
from app.repositories.registrations import RegistrationRepository
from app.models.registrations import Registrations
from app.api.v1.models.registration import RegistrationCreate

class RegistrationService:
    def __init__(self, repo: RegistrationRepository):
        self.repo = repo

    def create_registration(self, session: Session, payload: RegistrationCreate):

        # 1. Prevent duplicate registration
        existing = self.repo.find_by_trip_student(
            session, payload.trip_id, payload.student_id
        )

        if existing:
            raise ValueError("Student already registered for this trip")

        # 2. Map DTO → ORM (IMPORTANT: preserve types)
        reg = Registrations(**payload.model_dump(mode="python"))

        # 3. Save
        return self.repo.create(session, reg)