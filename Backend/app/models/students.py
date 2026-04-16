from datetime import date, datetime, timezone
from typing import Optional

from sqlmodel import SQLModel, Field

class Students(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)       # internal PK
    student_id: Optional[int] = Field(default=None, index=True)     # external/student system ID
    name: str
    date_of_birth: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))