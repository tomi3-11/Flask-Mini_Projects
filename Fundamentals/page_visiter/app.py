from flask import Flask, session, jsonify
import os
import secrets


app = Flask(__name__)

#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = secrets.token_hex(16)

"""
we shall have several routes with different roles
1. get the counter
2. increment
3. decrement
4. reset counter
5. clear the session
"""

@app.route("/api/counter", methods=["GET", "POST"])
def get_counter():
    if 'counter' not in session:
        session['counter'] = 0

    return jsonify({
        "counter": session['counter'],
        "session_id": session.sid if hasattr(session, 'sid') else 'unknown',
        "message": "Counter retrived successfully"
    }, 200)


@app.route("/api/counter/increment", methods=["GET"])
def increment_counter():
    if 'counter' in session:
        session['counter'] += 1
        
    return jsonify({
        "counter": session['counter'],
        "message": "Counter incremented successfully"
    }, 200)


@app.route("/api/counter/decrement", methods=["GET"])
def decrement_counter():
    if 'counter' in session and session['counter'] > 0:
        session['counter'] -= 1
        
    return jsonify({
        "counter": session['counter'],
        "message": "Counter decremented successfully"
    }, 200)

