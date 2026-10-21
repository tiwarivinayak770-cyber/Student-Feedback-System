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


import streamlit as st

import requests

# ----------------------------
# Check Admin Login
# ----------------------------
if not st.session_state.get("admin_logged_in", False):
    st.error("Please login as Admin.")
    st.stop()

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Admin Dashboard")
st.write(f"Welcome **{st.session_state['admin']['username']}**")

# ----------------------------
# Get Data
# ----------------------------
students = requests.get("http://127.0.0.1:8000/students").json()
faculty = requests.get("http://127.0.0.1:8000/faculty").json()
subjects = requests.get("http://127.0.0.1:8000/subjects").json()
feedback = requests.get("http://127.0.0.1:8000/feedback").json()

# ----------------------------
# Dashboard Cards
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("👨‍🎓 Students", len(students))
col2.metric("👨‍🏫 Faculty", len(faculty))
col3.metric("📚 Subjects", len(subjects))
col4.metric("📝 Feedback", len(feedback))

st.divider()

# ----------------------------
# Average Rating
# ----------------------------
if feedback:
    avg_rating = round(
        sum(f["overall"] for f in feedback) / len(feedback),
        2
    )

    st.metric("⭐ Average Overall Rating", avg_rating)

else:
    st.info("No feedback available.")

st.divider()

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("Admin Menu")

st.sidebar.page_link(
    "pages/Students.py",
    label="🎓 Manage Students"
)

st.sidebar.page_link(
    "pages/View_Feedback.py",
    label="📝 View Feedback"
)

st.sidebar.page_link(
    "pages/Analytics.py",
    label="📈 Analytics"
)

# ----------------------------
# Quick Buttons
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎓 Manage Students", use_container_width=True):
        st.switch_page("pages/Students.py")

with col2:
    if st.button("📝 View Feedback", use_container_width=True):
        st.switch_page("pages/View_Feedback.py")

with col3:
    if st.button("📈 Analytics", use_container_width=True):
        st.switch_page("pages/Analytics.py")

st.divider()

# ----------------------------
# Logout
# ----------------------------
if st.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.switch_page("pages/Admin_Login.py")


import pandas as pd

st.divider()

st.subheader("📝 Recent Feedback")

if feedback:

    df = pd.DataFrame(feedback)

    st.dataframe(
        df.tail(10),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No feedback available.")


st.divider()

st.subheader("🏆 Top Rated Faculty")

if feedback:

    df = pd.DataFrame(feedback)

    faculty_rating = (
        df.groupby("faculty_id")["overall"]
        .mean()
        .reset_index()
        .sort_values(
            by="overall",
            ascending=False
        )
    )

    st.dataframe(
        faculty_rating,
        use_container_width=True,
        hide_index=True
    )


st.divider()

st.subheader("📚 Subject Performance")

if feedback:

    subject_rating = (
        df.groupby("subject_id")["overall"]
        .mean()
        .reset_index()
        .sort_values(
            by="overall",
            ascending=False
        )
    )

    st.dataframe(
        subject_rating,
        use_container_width=True,
        hide_index=True
    )

positive = len(df[df["sentiment"] == "Positive"])
neutral = len(df[df["sentiment"] == "Neutral"])
negative = len(df[df["sentiment"] == "Negative"])

c1, c2, c3 = st.columns(3)

c1.success(f"😊 Positive : {positive}")
c2.warning(f"😐 Neutral : {neutral}")
c3.error(f"😞 Negative : {negative}")

