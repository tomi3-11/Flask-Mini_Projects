from flask import Flask

app = Flask(__name__)

@app.route("/user/<string:name>", methods=["GET", "POST"])
def get_name(name: str):
    return {
        "Message": f"Hello, {name.title()}."
    }, 200
