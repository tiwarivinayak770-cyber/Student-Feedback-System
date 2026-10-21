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
from datetime import date

# ----------------------------
# Check Login
# ----------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("Home.py")

student = st.session_state["student"]

st.title("📝 Submit Feedback")

# ----------------------------
# Get Faculty & Subjects
# ----------------------------
faculty = requests.get("http://127.0.0.1:8000/faculty").json()
subjects = requests.get("http://127.0.0.1:8000/subjects").json()

faculty_dict = {
    f["faculty_name"]: f["faculty_id"]
    for f in faculty
}

subject_dict = {
    s["subject_name"]: s["subject_id"]
    for s in subjects
}

faculty_name = st.selectbox(
    "Select Faculty",
    list(faculty_dict.keys())
)

subject_name = st.selectbox(
    "Select Subject",
    list(subject_dict.keys())
)

st.markdown("### Rate the Faculty (1 = Poor, 5 = Excellent)")

teaching = st.slider("Teaching", 1, 5, 5)
communication = st.slider("Communication", 1, 5, 5)
practical = st.slider("Practical Knowledge", 1, 5, 5)
notes = st.slider("Notes Quality", 1, 5, 5)
interaction = st.slider("Student Interaction", 1, 5, 5)
overall = st.slider("Overall Rating", 1, 5, 5)

comment = st.text_area("Comments")

# ----------------------------
# Submit
# ----------------------------
if st.button("Submit Feedback"):

    response = requests.post(
        "http://127.0.0.1:8000/submit-feedback",
        json={
            "student_id": student["student_id"],
            "faculty_id": faculty_dict[faculty_name],
            "subject_id": subject_dict[subject_name],
            "teaching": teaching,
            "communication": communication,
            "practical": practical,
            "notes": notes,
            "interaction": interaction,
            "overall": overall,
            "comment": comment,
            "date": str(date.today())
        }
    )

    if response.status_code == 200:
        st.success("✅ Feedback Submitted Successfully!")
    else:
        st.error("❌ Failed to submit feedback.")