import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    color = "red"
    errors = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        errors.append("⚠ Password must be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        errors.append("⚠ Password must include at least one uppercase letter (A-Z).")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        errors.append("⚠ Password must include at least one lowercase letter (a-z).")

    # Number Check
    if re.search(r"\d", password):
        strength += 1
    else:
        errors.append("⚠ Password must include at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        errors.append("⚠ Password must include at least one special character (!@#$%^&*).")

    # Determine Strength Level
    if strength == 1 or strength == 2:
        remarks = "Weak"
        color = "red"
    elif strength == 3:
        remarks = "Medium"
        color = "orange"
    elif strength >= 4:
        remarks = "Strong"
        color = "green"

    return remarks, color, errors

# Streamlit UI
st.set_page_config(page_title="🔐 Password Generator", page_icon="🔒", layout="centered")

st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🔐 Password Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #2ecc71;'>Created by Farhana Ahsan</h3>", unsafe_allow_html=True)

# User Input
password = st.text_input("Enter your password", type="password")
confirm_password = st.text_input("Confirm your password", type="password")

if password and confirm_password:
    if password == confirm_password:
        strength, color, errors = check_password_strength(password)

        # Show Strength Result
        st.markdown(f"<h2 style='text-align: center; color: {color};'> Password Strength: {strength} </h2>", unsafe_allow_html=True)

        # Show Errors If Password is Weak
        if errors:
            for error in errors:
                st.error(error)
    else:
        st.error("❌ Passwords do not match! Please enter the same password in both fields.")
