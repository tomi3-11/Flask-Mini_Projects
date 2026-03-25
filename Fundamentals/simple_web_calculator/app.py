from flask import Flask, request, render_template


# instance of the flask class
app = Flask(__name__)


# Routes
@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    result = ""

    if request.method == "POST":
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        operation = request.form.get("operation", "")

        if operation == "addition"
            result = num1 + num2
            return result
        elif operation == "subraction":
            result = num1 - num2
            return result
        if operation == "multiplication":
            result = num1 * num2
            return result
        elif operation == "division":
            if num2 == 0:
                result = f"ZeroDivisionError: {num2} cannot be divided by 0"
                return result
            result = num1 / num2
            return result

    return render_template("index.html", result=result)
