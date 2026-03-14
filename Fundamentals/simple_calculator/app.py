from flask import Flask

app = Flask(__name__)


@app.route("/cal/add/<int:num1>/<int:num2>", methods=["POST", "GET"])
def add(num1, num2):
    result = num1 + num2
    return {
        "Result": f"The sum of {num1} and {num2} is {result}."
    }

