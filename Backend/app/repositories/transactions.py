# app/repositories/transaction_repository.py

from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import Session, select

from app.models.transactions import Transactions, PaymentStatus
from app.repositories.interfaces import TransactionRepository as TransactionRepositoryInterface


class TransactionRepository(TransactionRepositoryInterface):

    def get(self, session: Session, txn_id: int) -> Optional[Transactions]:
        return session.get(Transactions, txn_id)

    def get_by_transaction_id(self, session: Session, transaction_id: str) -> Optional[Transactions]:
        return session.exec(
            select(Transactions).where(
                Transactions.transaction_id == transaction_id
            )
        ).first()

    def list(self, session: Session) -> List[Transactions]:
        return session.exec(select(Transactions)).all()

    def create(self, session: Session, txn: Transactions) -> Transactions:
        session.add(txn)
        session.commit()
        session.refresh(txn)
        return txn

    def update_status(
        self,
        session: Session,
        txn: Transactions,
        status: PaymentStatus,
        error_message: str = None
    ) -> Transactions:

        txn.status = status
        txn.error_message = error_message

        if status == PaymentStatus.SUCCESS:
            txn.completed_at = datetime.now(timezone.utc)

        session.add(txn)
        session.commit()
        session.refresh(txn)
        return txn