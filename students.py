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

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Management",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Admin Login Check
# -----------------------------
if not st.session_state.get("admin_logged_in", False):
    st.warning("Please login as Admin.")
    st.switch_page("pages/Admin_Login.py")

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Management")

# -----------------------------
# Load Students
# -----------------------------
try:
    response = requests.get(
        "http://127.0.0.1:8000/students"
    )

    if response.status_code == 200:
        students = response.json()
    else:
        st.error("Unable to load students.")
        st.stop()

except Exception as e:
    st.error(f"Cannot connect to FastAPI\n\n{e}")
    st.stop()

# -----------------------------
# Search
# -----------------------------
search = st.text_input("🔍 Search Student")

df = pd.DataFrame(students)

if search:
    df = df[
        df.astype(str)
        .apply(
            lambda row: row.str.lower().str.contains(search.lower()).any(),
            axis=1
        )
    ]

# -----------------------------
# Statistics
# -----------------------------
st.metric("Total Students", len(df))

# -----------------------------
# Display
# -----------------------------
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)