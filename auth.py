from sqlalchemy.orm import Session
from backend.models import Student, Admin
from backend.schemas import LoginRequest


# -----------------------------
# Student Login
# -----------------------------
def login_student(db: Session, login_data: LoginRequest):

    student = (
        db.query(Student)
        .filter(
            Student.student_id == login_data.student_id,
            Student.password == login_data.password
        )
        .first()
    )

    if student:
        return {
            "message": "Login Successful",
            "student_id": student.student_id,
            "name": student.name
        }

    return {
        "message": "Invalid Student ID or Password"
    }


# -----------------------------
# Admin Login
# -----------------------------
def admin_login(username: str, password: str, db: Session):

    admin = db.query(Admin).filter(
        Admin.username == username
    ).first()

    if admin is None:
        return None

    if admin.password != password:
        return None

    return admin