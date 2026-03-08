from flask import Flask

# Instance of the flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return {
        "message": "Hello world from flask :)"
    }
