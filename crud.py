from sqlalchemy.orm import Session
from backend import models


# ----------------------------
# Student
# ----------------------------
def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: str):
    return (
        db.query(models.Student)
        .filter(models.Student.student_id == student_id)
        .first()
    )


def create_student(db: Session, student):

    new_student = models.Student(
        student_id=student.student_id,
        name=student.name,
        roll_no=student.roll_no,
        email=student.email,
        password=student.password,
        gender=student.gender,
        department=student.department,
        year=student.year,
        semester=student.semester,
        division=student.division,
        batch=student.batch,
        cgpa=student.cgpa,
        attendance=student.attendance
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# ----------------------------
# Faculty
# ----------------------------
def get_faculty(db: Session):
    return db.query(models.Faculty).all()


# ----------------------------
# Subject
# ----------------------------
def get_subjects(db: Session):
    return db.query(models.Subject).all()


# ----------------------------
# Feedback
# ----------------------------
def get_feedback(db: Session):
    return db.query(models.Feedback).all()


def create_feedback(db: Session, feedback):

    new_feedback = models.Feedback(
        student_id=feedback.student_id,
        faculty_id=feedback.faculty_id,
        subject_id=feedback.subject_id,
        teaching=feedback.teaching,
        communication=feedback.communication,
        practical=feedback.practical,
        notes=feedback.notes,
        interaction=feedback.interaction,
        overall=feedback.overall,
        comment=feedback.comment,
        sentiment="Pending",
        date=feedback.date
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback


def get_student_feedback(db: Session, student_id: str):
    return (
        db.query(models.Feedback)
        .filter(models.Feedback.student_id == student_id)
        .all()
    )