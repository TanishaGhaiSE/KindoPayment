
from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field


class Registrations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    trip_id: int = Field(foreign_key="trips.id", index=True)
    student_id: int = Field(index=True)

    parent_name: str
    parent_email: Optional[str] = None
    parent_phone: Optional[str] = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )




