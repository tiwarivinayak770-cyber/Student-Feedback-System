from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import StudentCreate
from sqlalchemy import func

from backend import crud, models
from backend.database import SessionLocal, engine
from backend.auth import login_student, admin_login
from backend.schemas import (
    LoginRequest,
    FeedbackCreate,
    AdminLoginRequest,
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Feedback System API")


# -----------------------------
# Database Dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Student Feedback System API Running"
    }


# -----------------------------
# Students
# -----------------------------
@app.get("/students")
def students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# -----------------------------
# Faculty
# -----------------------------
@app.get("/faculty")
def faculty(db: Session = Depends(get_db)):
    return crud.get_faculty(db)


# -----------------------------
# Subjects
# -----------------------------
@app.get("/subjects")
def subjects(db: Session = Depends(get_db)):
    return crud.get_subjects(db)


# -----------------------------
# Feedback
# -----------------------------
@app.get("/feedback")
def feedback(db: Session = Depends(get_db)):
    return crud.get_feedback(db)


# -----------------------------
# Student Login
# -----------------------------
@app.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_student(db, data)


# -----------------------------
# Admin Login
# -----------------------------
@app.post("/admin-login")
def login_admin(
    request: AdminLoginRequest,
    db: Session = Depends(get_db)
):

    admin = admin_login(
        request.username,
        request.password,
        db
    )

    if admin is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    return {
        "message": "Login Successful",
        "username": admin.username
    }


# -----------------------------
# Submit Feedback
# -----------------------------
@app.post("/submit-feedback")
def submit_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    return crud.create_feedback(db, feedback)

@app.get("/student/{student_id}")
def get_student(student_id: str, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)

@app.get("/student-feedback/{student_id}")
def student_feedback(student_id: str, db: Session = Depends(get_db)):
    return crud.get_student_feedback(db, student_id)

@app.post("/students")
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)

# -----------------------------
# Analytics Dashboard
# -----------------------------
@app.get("/analytics")
def analytics(db: Session = Depends(get_db)):

    total_students = db.query(models.Student).count()

    total_faculty = db.query(models.Faculty).count()

    total_subjects = db.query(models.Subject).count()

    total_feedback = db.query(models.Feedback).count()

    avg_rating = (
        db.query(func.avg(models.Feedback.overall))
        .scalar()
    )

    positive = (
        db.query(models.Feedback)
        .filter(models.Feedback.sentiment == "Positive")
        .count()
    )

    negative = (
        db.query(models.Feedback)
        .filter(models.Feedback.sentiment == "Negative")
        .count()
    )

    neutral = (
        db.query(models.Feedback)
        .filter(models.Feedback.sentiment == "Neutral")
        .count()
    )

    return {
        "students": total_students,
        "faculty": total_faculty,
        "subjects": total_subjects,
        "feedback": total_feedback,
        "average_rating": round(avg_rating or 0, 2),
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }


from sqlalchemy import func

@app.get("/faculty-ratings")
def faculty_ratings(db: Session = Depends(get_db)):

    data = (
        db.query(
            models.Faculty.faculty_name,
            func.avg(models.Feedback.overall).label("average_rating")
        )
        .join(
            models.Feedback,
            models.Faculty.faculty_id == models.Feedback.faculty_id
        )
        .group_by(models.Faculty.faculty_name)
        .all()
    )

    return [
        {
            "faculty": row.faculty_name,
            "rating": round(row.average_rating, 2)
        }
        for row in data
    ]

@app.get("/feedback-trend")
def feedback_trend(db: Session = Depends(get_db)):

    data = (
        db.query(
            models.Feedback.date,
            func.count(models.Feedback.feedback_id).label("count")
        )
        .group_by(models.Feedback.date)
        .order_by(models.Feedback.date)
        .all()
    )

    return [
        {
            "date": row.date,
            "count": row.count
        }
        for row in data
    ]

# -----------------------------
# Feedback Trend
# -----------------------------
@app.get("/feedback-trend")
def feedback_trend(db: Session = Depends(get_db)):

    data = (
        db.query(
            models.Feedback.date,
            func.count(models.Feedback.feedback_id).label("count")
        )
        .group_by(models.Feedback.date)
        .order_by(models.Feedback.date)
        .all()
    )

    return [
        {
            "date": row.date,
            "count": row.count
        }
        for row in data
    ]

# -----------------------------
# Subject-wise Average Rating
# -----------------------------
@app.get("/subject-ratings")
def subject_ratings(db: Session = Depends(get_db)):

    data = (
        db.query(
            models.Subject.subject_name,
            func.avg(models.Feedback.overall).label("average_rating")
        )
        .join(
            models.Feedback,
            models.Subject.subject_id == models.Feedback.subject_id
        )
        .group_by(models.Subject.subject_name)
        .all()
    )

    return [
        {
            "subject": row.subject_name,
            "rating": round(row.average_rating, 2)
        }
        for row in data
    ]


# -----------------------------
# Subject-wise Average Rating
# -----------------------------
@app.get("/subject-ratings")
def subject_ratings(db: Session = Depends(get_db)):
    ...
    return [
        ...
    ]


# -----------------------------
# Feedback Details (Admin)
# -----------------------------
@app.get("/feedback-details")
def feedback_details(db: Session = Depends(get_db)):
    data = (
        db.query(
            models.Feedback.feedback_id,
            models.Student.student_id,
            models.Student.name,
            models.Subject.subject_name,
            models.Faculty.faculty_name,
            models.Feedback.overall,
            models.Feedback.comment,
            models.Feedback.date
        )
        .join(
            models.Student,
            models.Student.student_id == models.Feedback.student_id
        )
        .join(
            models.Subject,
            models.Subject.subject_id == models.Feedback.subject_id
        )
        .join(
            models.Faculty,
            models.Faculty.faculty_id == models.Feedback.faculty_id
        )
        .all()
    )

    return [
        {
            "feedback_id": row.feedback_id,
            "student_id": row.student_id,
            "student_name": row.name,
            "faculty": row.faculty_name,
            "subject": row.subject_name,
            "rating": row.overall,
            "comment": row.comment,
            "date": row.date
        }
        for row in data
    ]