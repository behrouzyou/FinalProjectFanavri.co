# Python Quiz Application

A desktop quiz application built with Tkinter and SQLite. The interface includes user registration/login and a question-and-answer workflow focused on Python and introductory AI concepts.

## Features
- Tkinter desktop interface
- SQLite storage for users and quiz questions
- Sample questions inserted when the question table is empty
- Registration and login
- Quiz question browsing and management UI

## Stack
- Python
- Tkinter and ttk
- SQLite
- Pillow for image handling

## Run locally
Requires Python. Install Pillow if needed:

```bash
python -m pip install Pillow
python question-app.py
```

The app creates or uses `users.db` in its working directory.

## Security note
This is an educational project. The current implementation stores passwords directly in SQLite; do not use it for real accounts without adding password hashing and reviewing authentication/data handling.
