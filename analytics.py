from theme import apply_theme

apply_theme()

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Analytics Dashboard")

# --------------------------------
# Load Analytics Data
# --------------------------------
try:
    response = requests.get(
        "http://127.0.0.1:8000/analytics"
    )

    analytics = response.json()

except Exception as e:

    st.error(f"Unable to connect to FastAPI\n\n{e}")
    st.stop()

# --------------------------------
# Dashboard Cards
# --------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("👨‍🎓 Students", analytics["students"])
col2.metric("👨‍🏫 Faculty", analytics["faculty"])
col3.metric("📚 Subjects", analytics["subjects"])
col4.metric("📝 Feedback", analytics["feedback"])

st.markdown("---")

col5, col6, col7, col8 = st.columns(4)

col5.metric("⭐ Average Rating", analytics["average_rating"])
col6.metric("😊 Positive", analytics["positive"])
col7.metric("😐 Neutral", analytics["neutral"])
col8.metric("😞 Negative", analytics["negative"])

# --------------------------------
# Faculty-wise Average Rating
# --------------------------------
st.markdown("---")
st.subheader("📊 Faculty-wise Average Rating")

try:

    response = requests.get(
        "http://127.0.0.1:8000/faculty-ratings"
    )

    faculty_data = response.json()

    df = pd.DataFrame(faculty_data)

    if not df.empty and "rating" in df.columns:

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(
            df["faculty"],
            df["rating"]
        )

        ax.set_xlabel("Faculty")
        ax.set_ylabel("Average Rating")
        ax.set_title("Faculty-wise Average Rating")

        plt.xticks(rotation=45)

        st.pyplot(fig)

    else:

        st.info("No faculty rating data available.")

except Exception as e:

    st.error(e)

# --------------------------------
# Sentiment Distribution
# --------------------------------
st.markdown("---")
st.subheader("🥧 Sentiment Distribution")

labels = ["Positive", "Neutral", "Negative"]

values = [
    analytics["positive"],
    analytics["neutral"],
    analytics["negative"]
]

if sum(values) > 0:

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Feedback Sentiment Distribution")

    st.pyplot(fig)

else:

    st.info("No sentiment data available.")

# --------------------------------
# Feedback Trend
# --------------------------------
st.markdown("---")
st.subheader("📈 Feedback Trend")

try:

    response = requests.get(
        "http://127.0.0.1:8000/feedback-trend"
    )

    trend_data = response.json()

    df = pd.DataFrame(trend_data)

    if not df.empty and "count" in df.columns:

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            df["date"].astype(str),
            df["count"].astype(int),
            marker="o",
            linewidth=2
        )

        ax.set_xlabel("Date")
        ax.set_ylabel("Feedback Count")
        ax.set_title("Daily Feedback Trend")

        plt.xticks(rotation=45)

        st.pyplot(fig)

    else:

        st.info("No feedback trend data available.")

except Exception as e:

    st.error(e)

# --------------------------------
# Subject-wise Average Rating
# --------------------------------
st.markdown("---")
st.subheader("📚 Subject-wise Average Rating")

try:

    response = requests.get(
        "http://127.0.0.1:8000/subject-ratings"
    )

    subject_data = response.json()

    df = pd.DataFrame(subject_data)

    if not df.empty and "rating" in df.columns:

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(
            df["subject"],
            df["rating"]
        )

        ax.set_xlabel("Subject")
        ax.set_ylabel("Average Rating")
        ax.set_title("Subject-wise Average Rating")

        plt.xticks(rotation=45)

        st.pyplot(fig)

    else:

        st.info("No subject rating data available.")

except Exception as e:

    st.error(e)

