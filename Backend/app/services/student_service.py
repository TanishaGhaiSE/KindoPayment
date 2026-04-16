# app/services/student_service.py

from datetime import datetime, timezone
from app.models.students import Students


class StudentService:

    def __init__(self, repo):
        self.repo = repo

    def create_student(self, session, name: str, date_of_birth=None, student_id=None):

        student = Students(
            name=name,
            date_of_birth=date_of_birth,
            student_id=student_id,
            created_at=datetime.now(timezone.utc),
        )

        return self.repo.create(session, student)

    def get_student(self, session, student_id: int):
        return self.repo.get(session, student_id)

    def list_students(self, session):
        return self.repo.list(session)

    def delete_student(self, session, student_id: int):
        student = self.repo.get(session, student_id)
        if not student:
            return None
        self.repo.delete(session, student)
        return True