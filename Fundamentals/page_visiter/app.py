from flask import Flask, session, request
import os


app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/users", methods=["GET", "POST"])
def user_session():
    pass
