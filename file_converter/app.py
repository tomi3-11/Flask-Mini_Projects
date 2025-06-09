from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for, abort
from werkzeug.utils import secure_filename
from pdf2docx import Converter
from docx2pdf import convert
import os
import threading
import time
import logging

app = Flask(__name__)
app.secret_key = "Your_secret_key_here" # Change to a secure in real use

UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Create upload folder if missing
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def cleanup_files(delay=300):
    while True:
        now = time.time()
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                age = now - os.path.getmtime(filepath)
                if age > delay:
                    try:
                        os.remove(filepath)
                        print(f"Deleted old file: {filename}")
                    except Exception as e:
                        print(f"Error deleting {filename}: {e}")
        time.sleep(delay)

cleanup_thread = threading.Thread(target=cleanup_files, daemon=True)
cleanup_thread.start()


@app.errorhandler(413)
def too_large(e):
    flash("File too large. Max size 16MB.")
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part.")
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            try:
                if filename.lower().endswith('.pdf'):
                    output_filename = filename.rsplit('.', 1)[0] + '.docx'
                    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                    cv = Converter(input_path)
                    cv.convert(output_path)
                    cv.close()
                elif filename.lower().endswith('.docx'):
                    output_filename = filename.rsplit('.', 1)[0] + '.pdf'
                    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                    convert(input_path, output_path)
                else:
                    flash("Unsupported file type:")
                    return redirect(request.url)

            except Exception as e:
                flash(f"Conversion failed: {str(e)}")
                return redirect(request.url)

            return redirect(url_for('download_file', filename=output_filename))

        else:
            flash("Allowed file types: pdf, docx")
            return redirect(request.url)

    return render_template('index.html')


@app.route('/uploads/<filename>')
def download_file(filename):
    if not allowed_file(filename):
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
