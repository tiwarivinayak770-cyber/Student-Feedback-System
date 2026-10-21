from pathlib import Path
import pandas as pd

from backend.database import SessionLocal, engine
from backend.models import Base, Student, Faculty, Subject, Feedback

# -----------------------------
# Create database tables
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# Dataset paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"

students_file = DATASET_DIR / "students_part1_1000 (1).csv"
faculty_file = DATASET_DIR / "faculty_part2 (2).csv"
subjects_file = DATASET_DIR / "subjects_part2 (1).csv"
feedback_file = DATASET_DIR / "feedback_5000 (1).csv"

# -----------------------------
# Read CSV files
# -----------------------------
students_df = pd.read_csv(students_file)
faculty_df = pd.read_csv(faculty_file)
subjects_df = pd.read_csv(subjects_file)
feedback_df = pd.read_csv(feedback_file)

print("✓ All datasets loaded successfully.")

db = SessionLocal()

# -----------------------------
# Import Students
# -----------------------------
print("Importing Students...")

for _, row in students_df.iterrows():
    db.merge(Student(
    student_id=str(row["Student_ID"]),
    name=row["Name"],
    roll_no=str(row["Roll_No"]),
    email=row["Email"],

    password="student123",   

    gender=row["Gender"],
    department=row["Department"],
    year=str(row["Year"]),
    semester=int(row["Semester"]),
    division=row["Division"],
    batch=row["Batch"],
    cgpa=float(row["CGPA"]),
    attendance=float(row["Attendance"])
))

db.commit()
print(f"✓ Imported {len(students_df)} students.")

# -----------------------------
# Import Faculty
# -----------------------------
print("Importing Faculty...")

for _, row in faculty_df.iterrows():
    db.merge(Faculty(
        faculty_id=str(row["Faculty_ID"]),
        faculty_name=row["Faculty_Name"],
        designation=row["Designation"],
        qualification=row["Qualification"],
        experience_years=int(row["Experience_Years"]),
        email=row["Email"],
        phone=str(row["Phone"])
    ))

db.commit()
print(f"✓ Imported {len(faculty_df)} faculty records.")

# -----------------------------
# Import Subjects
# -----------------------------
print("Importing Subjects...")

for _, row in subjects_df.iterrows():
    db.merge(Subject(
        subject_id=str(row["Subject_ID"]),
        subject_name=row["Subject_Name"],
        semester=int(row["Semester"]),
        credits=int(row["Credits"]),
        faculty_id=str(row["Faculty_ID"])
    ))

db.commit()
print(f"✓ Imported {len(subjects_df)} subjects.")

# -----------------------------
# Import Feedback
# -----------------------------
print("Importing Feedback...")

for _, row in feedback_df.iterrows():
    db.merge(Feedback(
        feedback_id=int(row["Feedback_ID"]),
        student_id=str(row["Student_ID"]),
        faculty_id=str(row["Faculty_ID"]),
        subject_id=str(row["Subject_ID"]),
        teaching=int(row["Teaching"]),
        communication=int(row["Communication"]),
        practical=int(row["Practical"]),
        notes=int(row["Notes"]),
        interaction=int(row["Interaction"]),
        overall=int(row["Overall"]),
        comment=row["Comment"],
        sentiment=row["Sentiment"],
        date=str(row["Date"])
    ))

db.commit()
print(f"✓ Imported {len(feedback_df)} feedback records.")

db.close()

print("\n" + "=" * 50)
print("DATABASE IMPORT COMPLETED SUCCESSFULLY")
print("=" * 50)