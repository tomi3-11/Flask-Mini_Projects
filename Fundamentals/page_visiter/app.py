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
        session.modified = True
        
    return jsonify({
        "counter": session['counter'],
        "message": "Counter incremented successfully"
    }, 200)


@app.route("/api/counter/decrement", methods=["GET"])
def decrement_counter():
    if 'counter' in session and session['counter'] > 0:
        session['counter'] -= 1
        session.modified = True
        
    return jsonify({
        "counter": session['counter'],
        "message": "Counter decremented successfully"
    }, 200)
    

@app.route("/api/counter/reset", methods=["GET"])
def reset_counter():
    session['counter'] = 0
    session.modified = True

    return jsonify({
        "session": session['counter'],
        "message": "session reset successfully"
    }, 200)


@app.route("/api/counter/clear", methods=["GET"])
def clear_session():
    session.clear()
    return jsonify({
        "message": "Session cleared successfully."
    }, 200)


@app.route("/api/counter/info/", methods=["GET"])
def get_session_info():
    return jsonify({
        "message": "Counter retrived successfully.",
        "session": session["counter"],
        "session_id": session.sid if hasattr(session, 'sid') else 'unknown',
    }, 200)
