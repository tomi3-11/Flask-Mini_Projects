# Flask Mini-Projects

A collection of small, self-contained Flask example applications and experiments. Each folder in this repository contains an individual mini-project demonstrating a focused Flask feature or pattern (forms, file handling, simple APIs, templates, and more).

Table of contents
- Project overview
- Repository structure
- Prerequisites
- Installation
- Running a project
- Project descriptions
- Contributing
- License

Project overview
This repository gathers multiple minimal Flask applications intended for learning, demonstration, and quick prototyping. Each project is intentionally small so it can be run independently and understood in isolation.

Repository structure
- file_converter: simple app to upload and convert files. Contains its own `requirements.txt` when needed.
- Fundamentals: assorted introductory apps (Form input, Hello world, page visitor counter, calculators, URL path examples).
- quiz_app: small quiz application with templates and result handling.
- Todo_list: a basic todo list CRUD web app with templates and `requirements.txt`.
- TodoAPI: minimal REST-style todo API example.
- youtube_downloader: simple UI for downloading YouTube content (educational/demo purposes).
- LICENSE: repository license file.

Prerequisites
- Python 3.8 or newer is recommended. These projects were developed and tested with modern Python 3.x interpreters.
- `pip` for installing dependencies.
- For network access (downloader examples) a working internet connection is required.

Installation (per project)
1. Open a terminal and change into the project folder you want to run, e.g.:

    cd file_converter

2. Create and activate a virtual environment (recommended):

    python -m venv .venv
    source .venv/bin/activate

3. If the project includes a `requirements.txt`, install dependencies:

    pip install -r requirements.txt

Running a project
Most mini-projects use a simple `app.py` Flask application. Two common ways to run:

- Using the Flask CLI (preferred when the app uses `flask run`):

  export FLASK_APP=app.py
  export FLASK_ENV=development   # optional
  flask run --port=5000

- Running directly with Python (works if the app contains a guarded run block):

  python app.py

If you need to run multiple projects at once, set different ports using `--port` or `app.run(port=XXXX)` in the script.

Project descriptions
- file_converter: Upload a file through a web form and perform a conversion or simple processing step. Check `templates/` for UI.
- Fundamentals/Form_input_app: Demonstrates handling simple form data in Flask.
- Fundamentals/helloWorld: Minimal "Hello, World" Flask example.
- Fundamentals/page_visiter: Demonstrates request handling and optionally simple visit counting.
- Fundamentals/simple_calculator: CLI or web-based simple arithmetic operations.
- Fundamentals/simple_web_calculator: Web form-based calculator with template UI.
- Fundamentals/url_path_info: Demonstrates capturing URL path parameters and query strings.
- quiz_app: Presents questions via templates and shows results on submission.
- Todo_list: Example CRUD application with server-side rendered templates.
- TodoAPI: Minimal REST endpoints (JSON) demonstrating API design patterns in Flask.
- youtube_downloader: Educational example showing how to integrate a downloader; exercise caution and follow platform terms of service when using.

Notes and best practices
- Use an isolated virtual environment per project to avoid dependency conflicts.
- Inspect each project's `requirements.txt` (if present) before installing.
- If a project uses third-party services or APIs, check for any required credentials and add them via environment variables — do not commit secrets.

Contributing
- Contributions and improvements are welcome. For small fixes or documentation changes, open a concise pull request describing the change.
- When adding or updating a mini-project, include a short README inside that project's directory describing how to run only that app and list any additional dependencies.

License
See the `LICENSE` file in the repository root for license details.

Contact and support
If you have questions about any example, please open an issue in this repository with the project name and a short description of the problem.

Acknowledgements
These mini-projects are intended as learning resources and starting points for further exploration of Flask and web development in Python.

---
Last updated: repository documentation
