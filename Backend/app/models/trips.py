from datetime import datetime, date, timezone
from decimal import Decimal
from typing import Optional

from sqlmodel import SQLModel, Field, Column
from sqlalchemy import Numeric


def utc_now():
    return datetime.now(timezone.utc)


class Trips(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: Optional[str] = Field(default=None, index=True)
    title: str
    date: date
    location: str
    cost: Decimal = Field(sa_column=Column(Numeric(10, 2)))
    description: Optional[str] = None
    activity_id: Optional[str] = Field(default=None, index=True)

    created_at: datetime = Field(default_factory=utc_now)