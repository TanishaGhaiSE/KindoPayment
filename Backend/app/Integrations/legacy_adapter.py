# app/gateways/legacy_adapter.py

from app.Integrations.legacy_payment import LegacyPaymentProcessor, PaymentResponse


class LegacyPaymentAdapter:

    def __init__(self):
        self.client = LegacyPaymentProcessor()

    def process_payment(self, payment_data: dict) -> PaymentResponse:

        try:
            return self.client.process_payment(payment_data)

        except ValueError as e:
            # 🔥 THIS IS THE KEY FIX
            return PaymentResponse(
                success=False,
                error_message=str(e),
                transaction_id=None
            )

        except Exception:
            return PaymentResponse(
                success=False,
                error_message="Unexpected legacy failure"
            )