import streamlit as st
st.title("User Management System")
st.text("You can create an account, log in, and manage your profile easily through this system. After signing in, you can update your account details or delete your account whenever needed. The application guides you with clear messages and validations to ensure a smooth and secure account management experience.")
st.text("Please create and account before moving ahead.")
if st.button("Sign up."):
    st.switch_page("pages/signup.py")