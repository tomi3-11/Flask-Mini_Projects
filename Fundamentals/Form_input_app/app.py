from flask import Flask, request

app = Flask(__name__)


@app.route("/api/search") 
def index():
    # Getting single value
    name = request.args.get('name', default='Guest', type=str)
    age = request.args.get('age', type=str)

    # get all the parameters as dict
    all_params = request.args.to_dict()

    return {
        "message": "sucessfully",
        "Details": all_params
    }, 200
    
