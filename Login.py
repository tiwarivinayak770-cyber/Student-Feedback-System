import streamlit as st
import requests

st.set_page_config(page_title="Student Login", page_icon="🎓")

st.title("🎓 Student Feedback System")
st.subheader("Student Login")

student_id = st.text_input("Student ID")
password = st.text_input("Password", type="password")

if st.button("Login"):

    response = requests.post(
        "http://127.0.0.1:8000/login",
        json={
            "student_id": student_id,
            "password": password
        }
    )

    data = response.json()

    if data["message"] == "Login Successful":
        st.success(f"Welcome {data['name']}")

        st.session_state["logged_in"] = True
        st.session_state["student"] = data

        st.switch_page("pages/Dashboard.py")

    else:
        st.error(data["message"])