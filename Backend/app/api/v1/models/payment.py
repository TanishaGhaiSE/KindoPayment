# app/schemas/payment.py

from pydantic import BaseModel, Field


class PaymentCreateRequest(BaseModel):
    student_name: str
    parent_name: str
    amount: float = Field(gt=0)
    card_number: str
    expiry_date: str
    cvv: str
    school_id: str
    activity_id: str