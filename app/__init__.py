
from flask import Flask
from config import Config
from app.extensions import db, migrate
from app import models
from flask import render_template


from app.models.account import Account
from app.models.category import Category
from app.models.transaction import Transaction
from app.models.transaction_allocation import TransactionAllocation



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize database extensions
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/health/database")
    def database_health():

        from sqlalchemy import text

        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT DATABASE()")
                )

                database_name = result.scalar()

            return {
                "status": "success",
                "database": database_name,
                "message": "Database connection successful"
            }

        except Exception as error:
            app.logger.exception("Database connection failed")

            return {
                "status": "error",
                "message": "Database connection failed"
            }, 500

    return app
