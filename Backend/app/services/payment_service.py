# app/services/payment_service.py

from datetime import datetime, timezone
from decimal import Decimal
import uuid

from app.Integrations.legacy_adapter import LegacyPaymentAdapter
from app.core.exception import AppException
from app.models.transactions import Transactions, PaymentStatus


class PaymentService:

    def __init__(self, repo):
        self.repo = repo
        self.gateway = LegacyPaymentAdapter()

    def create_payment(
        self,
        session,
        registration_id: int,
        trip_id: int,
        payload,
        currency="NZD"
    ):

        # ✅ Convert Pydantic → dict safely
        payload_dict = payload.model_dump()

        # 🔥 DEBUG (remove later)
        print("🔥 LEGACY PAYLOAD:", payload_dict)

        # ✅ Validate amount (business rule)
        amount = payload_dict.get("amount")
        if amount is None or amount <= 0:
            raise AppException(
                "Amount must be greater than 0",
                400,
                "INVALID_AMOUNT"
            )

        # ✅ Convert to Decimal (DB safety)
        amount = Decimal(str(amount))

        # 1. CALL LEGACY
        response = self.gateway.process_payment(payload_dict)

        # 2. HANDLE FAILURE (THIS TRIGGERS MIDDLEWARE)
        if not response.success:
            raise AppException(
                message=response.error_message or "Payment failed",
                status_code=400,
                code="LEGACY_PAYMENT_FAILED"
            )

        # 3. CREATE TRANSACTION (SUCCESS ONLY)
        payment = Transactions(
            transaction_id=response.transaction_id or str(uuid.uuid4()),
            registration_id=registration_id,
            trip_id=trip_id,
            amount=amount,
            currency=currency,
            status=PaymentStatus.SUCCESS,
            error_message=None,
            attempt_count=1,
            created_at=datetime.now(timezone.utc),
            completed_at=datetime.now(timezone.utc),
        )

        return self.repo.create(session, payment)

    # 🔍 GET PAYMENT
    def get_payment(self, session, payment_id: int):
        return self.repo.get(session, payment_id)

    # 📋 LIST PAYMENTS
    def list_payments(self, session):
        return self.repo.list(session)

    # ✅ MARK SUCCESS
    def mark_success(self, session, payment_id: int):
        payment = self.repo.get(session, payment_id)
        if not payment:
            raise AppException("Payment not found", 404, "PAYMENT_NOT_FOUND")

        payment.completed_at = datetime.now(timezone.utc)

        return self.repo.update_status(
            session,
            payment,
            PaymentStatus.SUCCESS
        )

    # ❌ MARK FAILED
    def mark_failed(self, session, payment_id: int, error: str):
        payment = self.repo.get(session, payment_id)
        if not payment:
            raise AppException("Payment not found", 404, "PAYMENT_NOT_FOUND")

        payment.completed_at = datetime.now(timezone.utc)

        return self.repo.update_status(
            session,
            payment,
            PaymentStatus.FAILED,
            error_message=error
        )