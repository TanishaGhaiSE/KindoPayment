# app/repositories/student_repository.py

from typing import List, Optional
from sqlmodel import Session, select

from app.models.students import Students
from app.repositories.interfaces import StudentRepository as StudentRepositoryInterface


class StudentRepository(StudentRepositoryInterface):

    def get(self, session: Session, student_id: int) -> Optional[Students]:
        return session.get(Students, student_id)

    def list(self, session: Session) -> List[Students]:
        return session.exec(select(Students)).all()

    def create(self, session: Session, student: Students) -> Students:
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    def delete(self, session: Session, student: Students):
        session.delete(student)
        session.commit()