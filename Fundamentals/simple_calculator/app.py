from flask import Flask

app = Flask(__name__)


@app.route("/cal/add/<int:num1>/<int:num2>", methods=["POST", "GET"])
def add(num1, num2):
    result = num1 + num2
    return {
        "Result": f"The sum of {num1} and {num2} is {result}."
    }

@app.route("/cal/subtract/<int:num1>/<int:num2>", methods=["POST", "GET"])
def subtract(num1, num2):
    result = num1 - num2
    return {
        "Result": f"The difference between {num1} and {num2} is {result}."
    }

@app.route("/cal/multiply/<int:num1>/<int:num2>", methods=["POST", "GET"])
def multiply(num1, num2):
    result = num1 * num2
    return {
        "Result": f"The product of {num1} and {num2} is {result}."
    }

@app.route("/cal/divide/<int:num1>/<int:num2>", methods=["POST", "GET"])
def divide(num1, num2):
    if num2 == 0:
        return {"error": f"ZeroDivisionError: Cannot divide {num1} by zero."}
    result = num1 / num2
    return {
        "Result": f"The sum of {num1} and {num2} is {result}."
    }

