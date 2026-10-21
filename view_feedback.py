import streamlit as st
import requests
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from theme import apply_theme

apply_theme()

st.set_page_config(
    page_title="View Feedback",
    page_icon="📝",
    layout="wide"
)

st.title("📝 View Feedback")

# -----------------------------
# Load Feedback Details
# -----------------------------
try:
    response = requests.get("http://127.0.0.1:8000/feedback-details")

    if response.status_code == 200:
        feedback = response.json()
    else:
        st.error("Unable to load feedback.")
        st.stop()

except Exception as e:
    st.error(f"Cannot connect to FastAPI\n\n{e}")
    st.stop()

# -----------------------------
# DataFrame
# -----------------------------
df = pd.DataFrame(feedback)

# -----------------------------
# Search
# -----------------------------
search = st.text_input("🔍 Search by Student, Faculty, Subject")

if search:
    df = df[
        df.astype(str)
        .apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]

# -----------------------------
# Rename Columns
# -----------------------------
df = df.rename(
    columns={
        "feedback_id": "Feedback ID",
        "student_id": "Student ID",
        "student_name": "Student Name",
        "faculty": "Faculty",
        "subject": "Subject",
        "rating": "Rating",
        "comment": "Comment",
        "date": "Date"
    }
)

# -----------------------------
# Show Table
# -----------------------------
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.success(f"Total Feedback Records : {len(df)}")

# -----------------------------
# Download CSV
# -----------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Feedback CSV",
    csv,
    "feedback_report.csv",
    "text/csv"
)