# Project list

Level 1: The Fundamentals

Focus: Routing, Templates, and Basic Logic

1. Hello World App
· Concept: Single route, returning a string.
· Why: Understand the simplest possible Flask application.
2. URL Path Info App
· Concept: Dynamic URL routing (e.g., /user/<name>).
· Why: Learn how to capture variables from the URL.
3. Simple Calculator (via URL)
· Concept: URL parameters (e.g., /add/5/3).
· Why: Perform logic based on URL variables and return the result.
4. Page Visit Counter
· Concept: Session management.
· Why: Learn how to persist data for a single user across requests.
5. Form Input App (GET)
· Concept: Query strings (request.args).
· Why: Capture data from a search form or URL parameters.
6. Simple Web Calculator (with Form)
· Concept: HTML form handling (POST method), request.form.
· Why: First interaction with user input via UI.
7. Random Quote Generator
· Concept: Rendering templates (render_template), passing variables.
· Why: Move from returning strings to proper HTML pages.
8. Simple To-Do List (In-Memory)
· Concept: Global list variable, basic CRUD (no database).
· Why: Understand how to manipulate data and reflect changes in the UI.

---

￼ Level 2: Database and Structure

Focus: Databases, Models, and User Management

1. Simple Blog (SQLite + SQL)
· Concept: Database integration (sqlite3), executing raw SQL.
· Why: First step into persistent data storage.
2. Blog with Flask-SQLAlchemy
· Concept: ORM (Object Relational Mapper), Models.
· Why: Learn to interact with the database using Python classes instead of raw SQL.
3. Todo App with Database
· Concept: Full CRUD with a database.
· Why: Apply database knowledge to a familiar to-do list structure.
4. User Registration System
· Concept: Password hashing (Werkzeug), user models.
· Why: Learn to securely store user credentials.
5. Login/Logout System
· Concept: Flask-Login extension, current_user.
· Why: Understand session-based authentication and protecting routes.
6. Personalized Todo App
· Concept: User-specific data (foreign keys).
· Why: Link tasks to a specific user so each person sees only their own todos.

---

￼ Level 3: Intermediate Features

Focus: File Handling, External APIs, and Advanced Patterns

1. Profile Picture Uploader
· Concept: File uploads, handling static files.
· Why: Learn to accept and serve user-uploaded files.
2. Contact Form with Email
· Concept: Flask-Mail extension.
· Why: Send emails from your application (e.g., contact form submissions).
3. Password Reset Feature
· Concept: Tokens (itsdangerous), background email tasks.
· Why: Implement a secure, real-world authentication flow.
4. Weather App (External API)
· Concept: requests library, consuming JSON APIs.
· Why: Fetch live data from a third-party service (like OpenWeatherMap).
5. News Aggregator
· Concept: Multiple API sources, environment variables (.env).
· Why: Combine data from different sources and secure API keys.
6. CSV Upload & Display
· Concept: Pandas (or csv module), data processing.
· Why: Accept a file, process it on the backend, and display the results.
7. Flash Messaging System
· Concept: Flask's flash() function.
· Why: Provide user feedback after actions (e.g., "Item saved successfully").
8. Admin Dashboard (Simple Stats)
· Concept: Database queries for counts/averages, admin-only routes.
· Why: Build a simple interface to monitor application data.

---

￼ Level 4: APIs and Advanced Logic

Focus: REST, Blueprints, and Complex Logic

1. Simple JSON API (Static Data)
· Concept: jsonify(), returning JSON instead of HTML.
· Why: Understand that Flask can serve data to other apps, not just browsers.
2. To-Do API (CRUD)
· Concept: RESTful principles (GET, POST, PUT, DELETE).
· Why: Build a pure backend API. (This is a frontend developer's dream backend).
3. API with Request Validation
· Concept: Marshmallow or custom validation.
· Why: Ensure data sent to your API is in the correct format.
4. API with Authentication (Token-Based)
· Concept: Flask-JWT-Extended, token generation/decorators.
· Why: Secure your API so only authorized users can access it.
5. Microblogging API (Posts/Users)
· Concept: Nested resources (e.g., /users/1/posts).
· Why: Model and expose relationships via API endpoints.
6. Blog with Blueprints
· Concept: Flask Blueprints.
· Why: Modularize your app (auth blueprint, main blueprint, admin blueprint).
7. Application Factory Pattern
· Concept: create_app() function.
· Why: Learn industry-standard structure for scalable Flask apps.

---

￼ Level 5: Real-World RESTful API Project

Focus: A complete, production-ready API

1. Library Management System API
· Endpoints: /books, /members, /loans
· Concepts:
· GET, POST, PUT, DELETE for resources.
· Relationships (A member loans a book).
· Query parameters (/books?author=Tolkien).
· Status codes (201 for created, 404 for not found).
· Error handling (consistent error JSON responses).
· Why: This ties everything together—database models, relationships, REST principles, and API design.
