from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ""


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"
