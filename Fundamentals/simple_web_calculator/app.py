from flask import Flask, request, render_template


# instance of the flask class
app = Flask(__name__)


# Routes
@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    result = None 

    if request.method == "POST":
        num1 = float(request.form.get("num1", ""))
        num2 = float(request.form.get("num2", ""))
        operation = request.form.get("operation", "")

        if operation == "addition":
            result = num1 + num2
        elif operation == "subraction":
            result = num1 - num2
        if operation == "multiplication":
            result = num1 * num2
        elif operation == "division":
            if num2 == 0:
                result = f"ZeroDivisionError: {num2} cannot be divided by 0"
            else:
                result = num1 / num2

    return render_template("index.html", result=result)
