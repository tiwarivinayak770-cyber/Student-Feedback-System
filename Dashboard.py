from theme import apply_theme

apply_theme()

import streamlit as st
import requests

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Check Login
# ----------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("Home.py")

# ----------------------------
# Get Logged-in Student
# ----------------------------
student = st.session_state.get("student", {})

student_name = student.get("name", "Student")
student_id = student.get("student_id", "Unknown")

# ----------------------------
# Debug (Temporary)
# ----------------------------
st.write("Session Student Data:", student)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.success(f"Welcome\n\n**{student_name}**")
    st.write(f"Student ID: {student_id}")

    st.page_link("pages/Profile.py", label="👤 Student Profile")

    if st.button("📝 My Feedback History"):
        st.switch_page("pages/My_Feedback.py")

    if st.button("📝 Submit Feedback"):
        st.switch_page("pages/Submit_Feedback.py")

    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("Home.py")

# ----------------------------
# Dashboard
# ----------------------------
st.title(f"📊 Welcome {student_name}")
st.write("Student Feedback System Dashboard")

# ----------------------------
# Load Data from FastAPI
# ----------------------------
students = requests.get("http://127.0.0.1:8000/students").json()
faculty = requests.get("http://127.0.0.1:8000/faculty").json()
subjects = requests.get("http://127.0.0.1:8000/subjects").json()
feedback = requests.get("http://127.0.0.1:8000/feedback").json()

# ----------------------------
# Metrics
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", len(students))
col2.metric("Faculty", len(faculty))
col3.metric("Subjects", len(subjects))
col4.metric("Feedback", len(feedback))

st.markdown("---")

st.subheader("🎯 Logged-in Student")

st.json(student)

