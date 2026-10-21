from sqlalchemy import Column, Integer, String, Float
from backend.database import Base


# ----------------------------
# Student Table
# ----------------------------
class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    roll_no = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    gender = Column(String)
    department = Column(String)
    year = Column(String)
    semester = Column(Integer)
    division = Column(String)
    batch = Column(String)

    cgpa = Column(Float)
    attendance = Column(Float)


# ----------------------------
# Faculty Table
# ----------------------------
class Faculty(Base):
    __tablename__ = "faculty"

    faculty_id = Column(String, primary_key=True, index=True)
    faculty_name = Column(String)
    designation = Column(String)
    qualification = Column(String)
    experience_years = Column(Integer)
    email = Column(String)
    phone = Column(String)


# ----------------------------
# Subject Table
# ----------------------------
class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(String, primary_key=True, index=True)
    subject_name = Column(String)
    semester = Column(Integer)
    credits = Column(Integer)
    faculty_id = Column(String)


# ----------------------------
# Feedback Table
# ----------------------------
class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True)

    student_id = Column(String)
    faculty_id = Column(String)
    subject_id = Column(String)

    teaching = Column(Integer)
    communication = Column(Integer)
    practical = Column(Integer)
    notes = Column(Integer)
    interaction = Column(Integer)
    overall = Column(Integer)

    comment = Column(String)
    sentiment = Column(String)
    date = Column(String)


# ----------------------------
# Admin Table
# ----------------------------
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


