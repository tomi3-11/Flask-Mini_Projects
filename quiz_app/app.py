from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "quiz_secret_key" # Needed for session

quiz = [
    {
        "question": "Which is the language of the WEB?",
        "options": ['English', 'JavaScript', 'Spanish', 'French'],
        "answer": "JavaScript"
    },
    {
        "question": "What is 7 x 8 ?",
        "options": ['54', '56', '47', '36'],
        "answer": "56"
    },
]

@app.route('/')
def index():
    session['current'] = 0
    session['score'] = 0
    return redirect(url_for('quiz_page'))


@app.route('/quiz', methods=["GET", "POST"])
def quiz_page():
    current = session.get("current", 0)
    score = session.get("score", 0)
    
    if request.method == "POST":
        selected = request.form.get('option')
        correct_answer = quiz[current - 1]['answer']
        if selected == correct_answer:
            score += 1
        session['score'] = score
    if current < len(quiz):
        question = quiz[current]
        session['current'] = current + 1
        
        return render_template("quiz.html", question=question, number=current + 1, total=len(quiz))
    else:  
        return redirect(url_for('result'))
    
    
@app.route('/result')
def result():
    return render_template("result.html", score=session.get('score', 0), total=len(quiz))


if __name__ == "__main__":
    app.run(debug=True)        
        
        