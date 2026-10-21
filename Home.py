from theme import apply_theme

apply_theme()
import streamlit as st
import requests

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Student Feedback System",
    page_icon="🎓",
    layout="centered"
)

# ----------------------------
# Redirect if already logged in
# ----------------------------
if st.session_state.get("logged_in", False):
    st.switch_page("pages/Dashboard.py")

# ----------------------------
# Title
# ----------------------------
st.title("🎓 Student Feedback System")
st.subheader("Student Login")
st.markdown("---")

# ----------------------------
# Login Form
# ----------------------------
student_id = st.text_input("Student ID")
password = st.text_input("Password", type="password")

# ----------------------------
# Login Button
# ----------------------------
if st.button("Login", use_container_width=True):

    if not student_id or not password:
        st.warning("Please enter Student ID and Password.")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/login",
                json={
                    "student_id": student_id,
                    "password": password
                },
                timeout=5
            )

            # Successful Login
            if response.status_code == 200:

                data = response.json()

                st.session_state["logged_in"] = True
                st.session_state["student"] = data

                st.success(f"Welcome {data['name']}")

                st.switch_page("pages/Dashboard.py")

            else:
                try:
                    error = response.json()
                    st.error(error.get("detail", "Invalid Username or Password"))
                except:
                    st.error("Login Failed.")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI Server.\n\nPlease start the backend first.")

        except Exception as e:
            st.error(f"Unexpected Error:\n{e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Student Feedback System | B.Sc. Data Science & AI Project")
