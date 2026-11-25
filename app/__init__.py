
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {
            "application": "MyMoney Manager",
            "message": "Welcome to MyMoney Manager!",
            "status": "running"
        }

    return app
