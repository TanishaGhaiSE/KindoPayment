from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from enum import Enum

from sqlmodel import SQLModel, Field, Column
from sqlalchemy import JSON, Numeric, Enum as SAEnum

class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Transactions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transaction_id: Optional[str] = Field(default=None, index=True)  # gateway ID
    registration_id: Optional[int] = Field(default=None, foreign_key="registrations.id", index=True)
    trip_id: Optional[int] = Field(default=None, foreign_key="trips.id", index=True)
    amount: Decimal = Field(sa_column=Column(Numeric(10, 2)))
    currency: str = Field(default="NZD", max_length=3)
    status: PaymentStatus = Field(sa_column=Column(SAEnum(PaymentStatus)), default=PaymentStatus.PENDING)
    error_message: Optional[str] = None
    attempt_count: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
