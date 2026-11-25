
from app.extensions import db
from datetime import datetime


class Account(db.Model):

    __tablename__ = "accounts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    account_type = db.Column(
        db.String(50),
        nullable=False
    )

    '''opening_balance = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0
    )'''

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    transactions = db.relationship(
        "Transaction",
        back_populates="account"
    )

    def __repr__(self):
        return f"<Account {self.name}>"
