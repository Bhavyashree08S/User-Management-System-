import streamlit as st
from db import connect_db
from validation import valid_password,valid_username
conn=connect_db()
cursor=conn.cursor()

st.title('Create Account Here!')

username=st.text_input("Enter the User name:")
password=st.text_input("Enter the Password:",type='password')
st.write("Password must be atleast 8 character long,must include uppercase,lowercase.digit,special charcter")
repass=st.text_input("Re-enter the password:",type='password')

if st.button("Signup"):
    if username == "" or password == "" or repass == "":
        st.error("All fields are required")
    elif not valid_username(username):
        st.warning("User name must be atleast 5 characters long!")
    elif password!=repass:
        st.error("Passwords do not match!")
    elif not valid_password(password):
        st.warning("Weak password")

    else:
        query="Select * from users where username=%s"
        values=(username,)
        cursor.execute(query,values)
        result=cursor.fetchone()
        if result:
            st.warning("Username already exists")
        else:
            insert_query="Insert into users(username,password) values(%s,%s)"
            insert_values=(username,password)
            cursor.execute(insert_query,insert_values)
            conn.commit()
            st.success("Account created Successfully!")
            st.switch_page("pages/login.py")
st.text("Already have an account")
if st.button("Login"):
    st.switch_page("pages/login.py")