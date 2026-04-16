from typing import Protocol

class PaymentGatewayInterface(Protocol):

    def process_payment(self, payment_data: dict):
        ...