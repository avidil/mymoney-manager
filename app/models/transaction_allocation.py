
from app.extensions import db


class TransactionAllocation(db.Model):

    __tablename__ = "transaction_allocations"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    transaction_id = db.Column(
        db.Integer,
        db.ForeignKey("transactions.id"),
        nullable=False
    )

    owner_type = db.Column(
        db.String(20),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    transaction = db.relationship(
        "Transaction",
        back_populates="allocations"
    )

    __table_args__ = (
        db.CheckConstraint(
            "owner_type IN ('PERSONAL', 'PARENTS')",
            name="check_allocation_owner"
        ),
        db.CheckConstraint(
            "amount > 0",
            name="check_allocation_amount_positive"
        ),
        db.UniqueConstraint(
            "transaction_id",
            "owner_type",
            name="unique_transaction_owner"
        ),
    )

    def __repr__(self):
        return f"<Allocation {self.owner_type}: {self.amount}>"
