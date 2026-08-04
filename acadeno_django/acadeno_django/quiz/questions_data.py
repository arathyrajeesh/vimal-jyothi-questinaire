"""
The canonical question bank: 3 questions per expected outcome, matching
the original front-end version of the outcomes check.
"""

QUESTIONS = [
    # Outcome 1 — Apply Python programming concepts
    {
        "outcome_code": "OUTCOME 1",
        "outcome_label": "OUTCOME 1 · PYTHON FUNDAMENTALS",
        "text": "What does this print?\n\nfor i in range(3):\n    print(i)",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "It raises an error"],
        "correct_index": 0,
    },
    {
        "outcome_code": "OUTCOME 1",
        "outcome_label": "OUTCOME 1 · PYTHON FUNDAMENTALS",
        "text": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "lambda"],
        "correct_index": 2,
    },
    {
        "outcome_code": "OUTCOME 1",
        "outcome_label": "OUTCOME 1 · PYTHON FUNDAMENTALS",
        "text": "What data type does Python's input() function always return?",
        "options": ["int", "str", "bool", "list"],
        "correct_index": 1,
    },

    # Outcome 2 — Design and develop dynamic web apps with Django
    {
        "outcome_code": "OUTCOME 2",
        "outcome_label": "OUTCOME 2 · DJANGO WEB DEVELOPMENT",
        "text": "Which file is primarily responsible for mapping URLs to views in a Django app?",
        "options": ["settings.py", "urls.py", "models.py", "manage.py"],
        "correct_index": 1,
    },
    {
        "outcome_code": "OUTCOME 2",
        "outcome_label": "OUTCOME 2 · DJANGO WEB DEVELOPMENT",
        "text": "What Django template tag allows a child template to inherit from a base layout?",
        "options": ["{% include %}", "{% inherit %}", "{% extends %}", "{% block %} alone"],
        "correct_index": 2,
    },
    {
        "outcome_code": "OUTCOME 2",
        "outcome_label": "OUTCOME 2 · DJANGO WEB DEVELOPMENT",
        "text": "Which command creates a new Django application inside a project?",
        "options": [
            "python manage.py startapp",
            "python manage.py newapp",
            "django-admin createapp",
            "python manage.py runapp",
        ],
        "correct_index": 0,
    },

    # Outcome 3 — CRUD with authentication and file handling
    {
        "outcome_code": "OUTCOME 3",
        "outcome_label": "OUTCOME 3 · DATABASE, CRUD & AUTH",
        "text": "Which Django component defines the structure of database tables using Python classes?",
        "options": ["Views", "Models", "Forms", "Middleware"],
        "correct_index": 1,
    },
    {
        "outcome_code": "OUTCOME 3",
        "outcome_label": "OUTCOME 3 · DATABASE, CRUD & AUTH",
        "text": "Which command applies pending model changes to the database schema?",
        "options": [
            "python manage.py migrate",
            "python manage.py makemigrations only",
            "python manage.py sync",
            "python manage.py update",
        ],
        "correct_index": 0,
    },
    {
        "outcome_code": "OUTCOME 3",
        "outcome_label": "OUTCOME 3 · DATABASE, CRUD & AUTH",
        "text": "What does Django's built-in auth system primarily handle?",
        "options": [
            "Image compression",
            "User registration, login and logout",
            "Database backups",
            "API rate limiting",
        ],
        "correct_index": 1,
    },

    # Outcome 4 — Integrate AI services
    {
        "outcome_code": "OUTCOME 4",
        "outcome_label": "OUTCOME 4 · AI INTEGRATION",
        "text": "What should never be hard-coded directly into source code when calling an AI API?",
        "options": ["The prompt text", "The API key", "The model name", "The response format"],
        "correct_index": 1,
    },
    {
        "outcome_code": "OUTCOME 4",
        "outcome_label": "OUTCOME 4 · AI INTEGRATION",
        "text": '"Prompt engineering" mainly refers to:',
        "options": [
            "Writing backend server code",
            "Designing database schemas",
            "Crafting inputs that guide an AI model toward a better output",
            "Compressing images before upload",
        ],
        "correct_index": 2,
    },
    {
        "outcome_code": "OUTCOME 4",
        "outcome_label": "OUTCOME 4 · AI INTEGRATION",
        "text": "In this bootcamp, which service powers the in-app AI features (summarisation, quizzes)?",
        "options": [
            "A local rule-based script",
            "Gemini / OpenAI API",
            "A spreadsheet macro",
            "Django admin",
        ],
        "correct_index": 1,
    },

    # Outcome 5 — Deploy and showcase
    {
        "outcome_code": "OUTCOME 5",
        "outcome_label": "OUTCOME 5 · DEPLOYMENT & PORTFOLIO",
        "text": "Which cloud platform was used to deploy the capstone project live?",
        "options": ["Render", "A personal USB drive", "Local host only", "Microsoft Word"],
        "correct_index": 0,
    },
    {
        "outcome_code": "OUTCOME 5",
        "outcome_label": "OUTCOME 5 · DEPLOYMENT & PORTFOLIO",
        "text": "Which tool tracks code changes and enables a clean commit history?",
        "options": ["Git", "Photoshop", "Excel", "Postman"],
        "correct_index": 0,
    },
    {
        "outcome_code": "OUTCOME 5",
        "outcome_label": "OUTCOME 5 · DEPLOYMENT & PORTFOLIO",
        "text": "Why does a public GitHub repository with clean commits matter for employability?",
        "options": [
            "It's required to install Python",
            "It demonstrates a professional development workflow to employers",
            "It automatically increases app speed",
            "It replaces the need for a resume",
        ],
        "correct_index": 1,
    },
]
