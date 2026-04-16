# app/api/v1/routes/student_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import Optional
from datetime import date

from app.db.database import get_session
from app.services.student_service import StudentService
from app.repositories.students import StudentRepository

router = APIRouter(prefix="/students", tags=["Students"])


def get_service():
    return StudentService(StudentRepository())


# ➕ CREATE STUDENT
@router.post("/")
def create_student(
    name: str,
    date_of_birth: Optional[date] = None,
    student_id: Optional[int] = None,
    session: Session = Depends(get_session),
    service: StudentService = Depends(get_service),
):
    return service.create_student(session, name, date_of_birth, student_id)


# 📋 GET ALL
@router.get("/")
def list_students(
    session: Session = Depends(get_session),
    service: StudentService = Depends(get_service),
):
    return service.list_students(session)


# 🔍 GET BY ID
@router.get("/{id}")
def get_student(
    id: int,
    session: Session = Depends(get_session),
    service: StudentService = Depends(get_service),
):
    student = service.get_student(session, id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student



# ❌ DELETE
@router.delete("/{id}")
def delete_student(
    id: int,
    session: Session = Depends(get_session),
    service: StudentService = Depends(get_service),
):
    result = service.delete_student(session, id)

    if not result:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted"}