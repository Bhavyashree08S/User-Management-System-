import streamlit as st
from db import connect_db
st.title("Login")
conn=connect_db()
cursor=conn.cursor()
username=st.text_input("Enter the user name:")
password=st.text_input("Enter the password:",type='password')
if st.button("Submit"):
   if username=="" or password=="":
     st.warning("All fields are required")
   else:
    query="select * from users where username=%s"
    values=(username,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result is None:
        st.error("Username Does not exists")
    else:
        db_password=result[2]
        if password==db_password:
            st.success("Login successfull")
            st.session_state["username"]=username
            st.switch_page("pages/welcome.py")
        else:
            st.error("Incorrect password")
