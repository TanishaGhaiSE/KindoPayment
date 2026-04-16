# app/api/v1/schemas/registration.py

from pydantic import BaseModel, EmailStr
from typing import Optional


class RegistrationCreate(BaseModel):
    trip_id: int
    student_id: int
    parent_name: str
    parent_email: Optional[EmailStr] = None
    parent_phone: Optional[str] = None