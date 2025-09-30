from flask import Flask, request, flash, render_template, url_for, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configurations
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# Initializations
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))

@app.route('/')
def home():
    return render_template('home.html') 
    
@app.route('/view')
def view_tasks():
    todos = Task.query.all()
    return render_template('view_tasks.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == "POST":
        title = request.form.get('title').strip()
        description = request.form.get('description').strip()
        
        if not title or not description:
            flash('Title and description are required', 'error')
            return render_template('create_task.html')
        
        new_task = Task(
            title=title,
            description=description
        )
        db.session.add(new_task)
        db.session.commit()
        
        flash('Task created successfully', 'success')
        return redirect(url_for('view-tasks'))
    return render_template('create_task.html', title=title, description=description)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        
        if not task.title or not task.description:
            flash('Title and description are required', 'error')
            return redirect(url_for('view_tasks'))
        
        db.session.commit()
        flash('Task updated successfully', 'success')
        return redirect(url_for('view_tasks'))
    
    return render_template('edit_task.html', task=task)


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('view_tasks'))
    
    


# Entry point
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)