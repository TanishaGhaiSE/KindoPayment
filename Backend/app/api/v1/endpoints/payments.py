# app/api/v1/routes/payment_routes.py

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.v1.models.payment import PaymentCreateRequest
from app.db.database import get_session
from app.services.payment_service import PaymentService
from app.repositories.transactions import TransactionRepository

router = APIRouter(prefix="/payments", tags=["Payments"])


# 🔧 Dependency Injection
def get_payment_service():
    return PaymentService(TransactionRepository())


# 💳 CREATE PAYMENT
@router.post("/")
def create_payment(
    registration_id: int,
    trip_id: int,
    payload: PaymentCreateRequest,
    session: Session = Depends(get_session),
    service: PaymentService = Depends(get_payment_service),
):
    return service.create_payment(
        session=session,
        registration_id=registration_id,
        trip_id=trip_id,
        payload=payload,   # pass object, service will handle
    )


# 🔍 GET PAYMENT BY ID
@router.get("/{payment_id}")
def get_payment(
    payment_id: int,
    session: Session = Depends(get_session),
    service: PaymentService = Depends(get_payment_service),
):
    payment = service.get_payment(session, payment_id)

    if not payment:
        from Backend.app.core.exception import AppException
        raise AppException("Payment not found", 404, "PAYMENT_NOT_FOUND")

    return payment


# 📋 LIST ALL PAYMENTS
@router.get("/")
def list_payments(
    session: Session = Depends(get_session),
    service: PaymentService = Depends(get_payment_service),
):
    return service.list_payments(session)


# ✅ MARK PAYMENT SUCCESS
@router.post("/{payment_id}/success")
def mark_success(
    payment_id: int,
    session: Session = Depends(get_session),
    service: PaymentService = Depends(get_payment_service),
):
    return service.mark_success(session, payment_id)


# ❌ MARK PAYMENT FAILED
@router.post("/{payment_id}/failed")
def mark_failed(
    payment_id: int,
    error: str,
    session: Session = Depends(get_session),
    service: PaymentService = Depends(get_payment_service),
):
    return service.mark_failed(session, payment_id, error)