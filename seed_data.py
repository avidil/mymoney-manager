
from app import create_app
from app.extensions import db
from app.models import Account, Category

app = create_app()

accounts = [
    ("Wallet", "CASH"),
    ("Bank Account", "BANK"),
    ("Money Market", "INVESTMENT"),
    ("Emergency Fund", "SAVINGS"),
    ("Uber Account", "DIGITAL_WALLET"),
]

income_categories = [
    "Salary",
    "Parents Contribution",
    "Other Income",
    "Refund / Reimbursement",
]

expense_categories = [
    "Food",
    "Transport",
    "Daily Needs",
    "Education",
    "Health",
    "Shopping",
    "Entertainment",
    "Bills",
    "Other Expense",
]

with app.app_context():
    try:
        # Insert accounts without creating duplicates
        for name, account_type in accounts:
            existing = Account.query.filter_by(name=name).first()

            if existing is None:
                db.session.add(
                    Account(name=name, account_type=account_type)
                )

        # Insert income categories
        for name in income_categories:
            existing = Category.query.filter_by(name=name).first()

            if existing is None:
                db.session.add(
                    Category(name=name, category_type="INCOME")
                )

        # Insert expense categories
        for name in expense_categories:
            existing = Category.query.filter_by(name=name).first()

            if existing is None:
                db.session.add(
                    Category(name=name, category_type="EXPENSE")
                )

        db.session.commit()

        print("Initial data inserted successfully!")
        print(f"Accounts: {Account.query.count()}")
        print(f"Categories: {Category.query.count()}")

    except Exception:
        db.session.rollback()
        raise

    finally:
        db.session.remove()
