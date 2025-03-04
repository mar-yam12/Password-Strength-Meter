import re;
import streamlit as st;

# Page Styling
st.set_page_config(
    page_title="Password Strength Checker By Maryam Shahid",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# Custom CSS
st.markdown(
"""
    <style>
    .main {
        background-color: #f0f2f6;
        text-align: center;
    }
    .stTextInput {
        width: 60% !important;
        margin: auto;
    }
    .stButton button{
        width: 50%;
        background-color: #007bff;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
        margin: 10px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🔐Password Strength Checker");
st.write("Check the strength of your password🔎");

# function to check password strength
def check_password_strength(password):
    score = 0;
    feedback = [];

    if len(password) >= 8:
        score += 1;
    else:
        feedback.append("🙅🏻Password should be at least 8 characters long");

    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password):
        score += 1;
    else:
        feedback.append("🙅🏻Password should contain at least one uppercase and one lowercase letter");

    if re.search(r'[0-9]', password):
        score += 1;
    else:
        feedback.append("🙅🏻Password should contain at least one number");

    if re.search(r'[!@#$%^&*()]', password):
        score += 1;
    else:
        feedback.append("🙅🏻Password should contain at least one special character");

    # display password strength
    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*()]', password):
        score += 1;
        st.success("✔️** Strong Password ** - You are good to go");
    elif re.search(r'[A-Z]', password) and re.search(r"[a-z]", password) and re.search(r'[0-9]', password):
        score += 1;
        st.warning("🚨**Moderate Password** - Try to add a special character for more security");
    else:
        st.error("😔**Weak Password** - Follow the Suggestion below to strengthen your password");
    
    return feedback;

# Password Input
password = st.text_input("Enter your password", type="password", placeholder="Enter your password", key="password",help="Password should be at least 8 characters long, contain at least one uppercase and one lowercase letter, one number and one special character");

# Check Password Strength
if st.button("Check Password Strength"):
    if password:
        feedback = check_password_strength(password);
        # Feedback Section
        if feedback:
            with st.expander("**Improve Your Password**"):
                for item in feedback:
                    st.write(item);
    else:
        st.warning("⚠️Please enter a password to check its strength");

