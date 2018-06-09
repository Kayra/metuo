from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@postgres:5432/metuo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    @app.route("/")
    @app.route("/index")
    def index():
        return "Hello world"

    return app
