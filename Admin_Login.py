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

st.set_page_config(
    page_title="Admin Login",
    page_icon="👨‍💼",
    layout="centered"
)

st.title("👨‍💼 Admin Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):

    if not username or not password:
        st.warning("Please enter Username and Password.")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/admin-login",
                json={
                    "username": username,
                    "password": password
                },
                timeout=5
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["admin_logged_in"] = True
                st.session_state["admin"] = data

                st.success("Admin Login Successful")

                st.switch_page("pages/Admin_Dashboard.py")

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