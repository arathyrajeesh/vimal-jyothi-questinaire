# Acadeno — Bootcamp Outcomes Check (Django)

A Django port of the original single-file HTML/JS quiz app for Acadeno
Technologies' AI-Integrated Python & Django Bootcamp. Same look, same 15
questions across 5 outcomes, same staff review screen — now with a real
backend, database-backed submissions, and Django admin.

## What changed vs. the JS version

- **State**: quiz progress (current question, in-progress answers) lives in
  the Django **session** instead of a JS `state` object, so it survives a
  page refresh and works with JS disabled (the option buttons and Next/Back
  are plain form submits under the hood).
- **Storage**: submissions are rows in a real `Submission` model (SQLite by
  default) instead of `window.storage`. Questions are a `Question` model,
  seeded automatically by a migration so `migrate` alone gets you a working
  app.
- **Staff review**: same access-code gate (`acadeno2026` by default), now
  backed by a session flag and a real query instead of a JS `fetch`-style
  list/get loop. Submissions are also browsable/exportable via `/admin/`.
- **Scoring**: computed server-side in `quiz/views.py` when the last question
  is submitted, mirroring the original's `outcomeBreakdown()` logic.

## Project layout

```
acadeno_django/
├── manage.py
├── requirements.txt
├── acadeno_outcomes/        # project settings, root urls
└── quiz/                    # the app
    ├── models.py            # Question, Submission
    ├── views.py             # landing → quiz → done, staff gate → list
    ├── urls.py
    ├── admin.py             # read-only Submission list, editable Questions
    ├── questions_data.py    # the 15-question seed bank
    ├── migrations/
    │   ├── 0001_initial.py
    │   └── 0002_seed_questions.py   # auto-seeds questions on migrate
    ├── management/commands/reseed_questions.py
    ├── templates/quiz/
    └── static/quiz/style.css
```

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate          # creates db.sqlite3 and seeds 15 questions
python manage.py createsuperuser  # optional, for /admin/
python manage.py runserver
```

Then visit:

- `http://127.0.0.1:8000/` — the quiz
- `http://127.0.0.1:8000/staff/` — staff review (code: `acadeno2026`)
- `http://127.0.0.1:8000/admin/` — Django admin (needs superuser)

## Configuration

Two things you'll want to change before deploying for real:

- `STAFF_ACCESS_CODE` in `acadeno_outcomes/settings.py` — reads from the
  `STAFF_ACCESS_CODE` env var, defaults to `acadeno2026`.
- `SECRET_KEY` and `DEBUG` — set `DJANGO_SECRET_KEY` and `DJANGO_DEBUG=False`
  via environment variables in production; the current defaults are for
  local development only.

To edit or add questions, either use `/admin/` or edit
`quiz/questions_data.py` and run:

```bash
python manage.py reseed_questions
```

(This wipes and rebuilds the `Question` table from that file — it does not
touch existing `Submission` records.)
