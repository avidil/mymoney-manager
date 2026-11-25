
from app.extensions import db
from datetime import datetime


class Transaction(db.Model):

    __tablename__ = "transactions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=True
    )

    transaction_type = db.Column(
        db.String(20),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    transaction_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    account = db.relationship(
        "Account",
        back_populates="transactions"
    )

    category = db.relationship(
        "Category",
        back_populates="transactions"
    )

    allocations = db.relationship(
        "TransactionAllocation",
        back_populates="transaction",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        db.CheckConstraint(
            "amount > 0",
            name="check_transaction_amount_positive"
        ),
        db.CheckConstraint(
            "transaction_type IN ('INCOME', 'EXPENSE', 'OPENING_BALANCE')",
            name="check_transaction_type"
        ),
    )

    def __repr__(self):
        return f"<Transaction {self.id} - {self.transaction_type}>"
