# Student Feedback System

A Student Feedback System built using FastAPI, Streamlit, SQLite, SQLAlchemy, and Python.

## Features

- Student Login
- Admin Login
- Submit Feedback
- My Feedback
- Analytics Dashboard
- Faculty-wise Ratings
- Subject-wise Ratings
- Feedback Trends
- CSV Export

## Technologies

- Python
- FastAPI
- Streamlit
- SQLite
- SQLAlchemy
- Pandas
- Matplotlib

## Installation

```bash
git clone <repository-url>
cd Student_Feedback_System
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn backend.app:app --reload
```

## Run Streamlit

```bash
cd frontend
streamlit run Home.py
```