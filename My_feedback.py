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
import pandas as pd

st.set_page_config(
    page_title="My Feedback",
    page_icon="📝",
    layout="wide"
)

# ----------------------------
# Check Login
# ----------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("Home.py")

# ----------------------------
# Logged-in Student
# ----------------------------
student = st.session_state["student"]
student_id = student["student_id"]

# ----------------------------
# Fetch Feedback
# ----------------------------
try:

    response = requests.get(
        f"http://127.0.0.1:8000/student-feedback/{student_id}"
    )

    if response.status_code == 200:
        feedback = response.json()
    else:
        feedback = []

except Exception as e:
    st.error(f"Unable to connect to FastAPI\n\n{e}")
    st.stop()

# ----------------------------
# Page Title
# ----------------------------
st.title("📝 My Feedback History")

st.write(f"Logged in as: **{student['name']} ({student_id})**")

st.markdown("---")

# ----------------------------
# Summary
# ----------------------------
st.metric("Total Feedback Submitted", len(feedback))

st.markdown("---")

# ----------------------------
# Table
# ----------------------------
if len(feedback) == 0:

    st.info("You haven't submitted any feedback yet.")

else:

    df = pd.DataFrame(feedback)

    df = df[
        [
            "feedback_id",
            "subject_id",
            "faculty_id",
            "overall",
            "sentiment",
            "comment",
            "date"
        ]
    ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )