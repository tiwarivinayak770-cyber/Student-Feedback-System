import streamlit as st
import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from theme import apply_theme

# Apply the theme
apply_theme()

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

# Rest of your code...

import streamlit as st
import requests

st.set_page_config(page_title="Student Login", page_icon="🎓")

st.title("🎓 Student Login")

st.markdown("---")

student_id = st.text_input("Student ID")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if student_id == "":
        st.error("Please enter Student ID")
    else:
        st.success(f"Welcome {student_id}")


import streamlit as st
import requests

# ----------------------------
# Check Login
# ----------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("Home.py")

# ----------------------------
# Get Logged-in Student
# ----------------------------
student_id = st.session_state["student"]["student_id"]

# ----------------------------
# Fetch Student Details
# ----------------------------
response = requests.get(
    f"http://127.0.0.1:8000/student/{student_id}"
)

student = response.json()

# ----------------------------
# Page
# ----------------------------
st.set_page_config(
    page_title="Student Profile",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("👨‍🎓 Student Profile")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Student ID", student["student_id"], disabled=True)
    st.text_input("Name", student["name"], disabled=True)
    st.text_input("Roll No", student["roll_no"], disabled=True)
    st.text_input("Email", student["email"], disabled=True)
    st.text_input("Gender", student["gender"], disabled=True)
    st.text_input("Department", student["department"], disabled=True)

with col2:
    st.text_input("Year", student["year"], disabled=True)
    st.text_input("Semester", student["semester"], disabled=True)
    st.text_input("Division", student["division"], disabled=True)
    st.text_input("Batch", student["batch"], disabled=True)
    st.text_input("CGPA", student["cgpa"], disabled=True)
    st.text_input("Attendance", student["attendance"], disabled=True)