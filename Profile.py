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

# ----------------------------
# Check Login
# ----------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("Home.py")

student = st.session_state["student"]

# ----------------------------
# Get Student Data
# ----------------------------
response = requests.get("http://127.0.0.1:8000/students")

students = response.json()

profile = None

for s in students:
    if s["student_id"] == student["student_id"]:
        profile = s
        break

# ----------------------------
# Page
# ----------------------------
st.title("👤 Student Profile")

if profile:

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Student ID", profile["student_id"], disabled=True)
        st.text_input("Name", profile["name"], disabled=True)
        st.text_input("Roll No", profile["roll_no"], disabled=True)
        st.text_input("Email", profile["email"], disabled=True)
        st.text_input("Gender", profile["gender"], disabled=True)
        st.text_input("Department", profile["department"], disabled=True)

    with col2:
        st.text_input("Year", profile["year"], disabled=True)
        st.text_input("Semester", profile["semester"], disabled=True)
        st.text_input("Division", profile["division"], disabled=True)
        st.text_input("Batch", profile["batch"], disabled=True)
        st.text_input("CGPA", profile["cgpa"], disabled=True)
        st.text_input("Attendance", profile["attendance"], disabled=True)

else:
    st.error("Student profile not found.")