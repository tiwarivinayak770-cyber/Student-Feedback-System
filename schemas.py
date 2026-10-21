from pydantic import BaseModel, ConfigDict


# ----------------------------
# Student Schema
# ----------------------------
class StudentBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    student_id: str
    name: str
    roll_no: str
    email: str
    password: str

    gender: str
    department: str
    year: str
    semester: int
    division: str
    batch: str

    cgpa: float
    attendance: float


class StudentCreate(BaseModel):

    student_id: str
    name: str
    roll_no: str
    email: str
    password: str

    gender: str
    department: str
    year: str
    semester: int
    division: str
    batch: str

    cgpa: float
    attendance: float


# ----------------------------
# Faculty Schema
# ----------------------------
class FacultyBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    faculty_id: str
    faculty_name: str
    designation: str
    qualification: str
    experience_years: int
    email: str
    phone: str


# ----------------------------
# Subject Schema
# ----------------------------
class SubjectBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    subject_id: str
    subject_name: str
    semester: int
    credits: int
    faculty_id: str


# ----------------------------
# Feedback Schema
# ----------------------------
class FeedbackBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    feedback_id: int
    student_id: str
    faculty_id: str
    subject_id: str

    teaching: int
    communication: int
    practical: int
    notes: int
    interaction: int
    overall: int

    comment: str
    sentiment: str
    date: str


class FeedbackCreate(BaseModel):

    student_id: str
    faculty_id: str
    subject_id: str

    teaching: int
    communication: int
    practical: int
    notes: int
    interaction: int
    overall: int

    comment: str
    date: str


# ----------------------------
# Student Login
# ----------------------------
class LoginRequest(BaseModel):

    student_id: str
    password: str


class LoginResponse(BaseModel):

    message: str
    student_id: str
    name: str


# ----------------------------
# Admin Login
# ----------------------------
class AdminLoginRequest(BaseModel):

    username: str
    password: str


class AdminLoginResponse(BaseModel):

    message: str
    username: str