
from app.extensions import db


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    category_type = db.Column(
        db.String(20),
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    transactions = db.relationship(
        "Transaction",
        back_populates="category"
    )

    def __repr__(self):
        return f"<Category {self.name}>"
