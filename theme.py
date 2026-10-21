import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    .main{
        background-color:#F5F7FA;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    h1{
        color:#0E4D92;
    }

    h2{
        color:#1565C0;
    }

    h3{
        color:#1976D2;
    }

    .stButton>button{
        width:100%;
        border-radius:10px;
        height:45px;
        font-size:16px;
        font-weight:bold;
    }

    div[data-testid="metric-container"]{
        background:white;
        border-radius:15px;
        padding:15px;
        box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    }

    </style>
    """, unsafe_allow_html=True)