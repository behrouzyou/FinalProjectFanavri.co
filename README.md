# Python Quiz Application

A desktop quiz application built with Python's Tkinter GUI toolkit and SQLite. The interface includes user registration/login and a question-and-answer workflow focused on Python and introductory AI concepts.

## Features
- Tkinter desktop interface
- SQLite storage for users and quiz questions
- Sample questions inserted when the questions table is empty
- Register and log in to access the quiz interface
- Add/view quiz questions through the application interface

## Tech stack
- Python
- Tkinter and ttk
- SQLite
- Pillow for image handling

## Run locally
Requires Python. Install Pillow if it is not already available:

```bash
python -m pip install Pillow
python question-app.py
```

The application creates/uses `users.db` in its working directory.

## Security note
This is an educational project. The current implementation stores passwords directly in SQLite; do not use it for real accounts without implementing password hashing and reviewing authentication and data handling.
