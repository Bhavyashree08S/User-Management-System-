import streamlit as st
from db import connect_db
from validation import valid_username,valid_password

@st.dialog("Update Account")
def update_popup():

    option = st.radio(
        "Choose Update Type",
        ["Username-Password", "Password"]
    )

    if option == "Username-Password":

        with st.form("update_user_pass_form"):

            new_username = st.text_input(
                "Enter the New Username"
            )

            old_password = st.text_input(
                "Enter the Old Password",
                type="password"
            )

            new_pass = st.text_input(
                "Enter the New Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Update Username and Password"
            )

            if submitted:

                if not valid_username(new_username):

                    st.warning(
                        "Username must be at least 5 characters long!"
                    )

                elif not valid_password(new_pass):

                    st.error("Weak Password")

                else:

                    old_query = """
                    SELECT * FROM users
                    WHERE username=%s
                    """

                    cursor.execute(
                        old_query,
                        (st.session_state["username"],)
                    )

                    results = cursor.fetchone()

                    if results is None:

                        st.error("User not found")

                    else:

                        db_password = results[2]

                        if old_password != db_password:

                            st.warning(
                                "Incorrect Password"
                            )

                        else:

                            check_query = """
                            SELECT * FROM users
                            WHERE username=%s
                            """

                            cursor.execute(
                                check_query,
                                (new_username,)
                            )

                            existing_user = cursor.fetchone()

                            if (
                                existing_user
                                and new_username
                                != st.session_state["username"]
                            ):

                                st.warning(
                                    "Username already exists"
                                )

                            else:

                                update_query = """
                                UPDATE users
                                SET username=%s,
                                    password=%s
                                WHERE username=%s
                                """

                                cursor.execute(
                                    update_query,
                                    (
                                        new_username,
                                        new_pass,
                                        st.session_state["username"]
                                    )
                                )

                                conn.commit()

                                st.session_state[
                                    "username"
                                ] = new_username

                                st.success(
                                    "Username and Password Updated Successfully"
                                )

    elif option == "Password":

        with st.form("update_password_form"):

            old_password = st.text_input(
                "Enter the Old Password",
                type="password"
            )

            new_pass = st.text_input(
                "Enter the New Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Update Password"
            )

            if submitted:

                cursor.execute(
                    """
                    SELECT * FROM users
                    WHERE username=%s
                    """,
                    (st.session_state["username"],)
                )

                results = cursor.fetchone()

                if results is None:

                    st.error("User not found")

                else:

                    db_password = results[2]

                    if old_password != db_password:

                        st.warning(
                            "Incorrect Password"
                        )

                    elif not valid_password(new_pass):

                        st.error(
                            "Weak Password"
                        )

                    else:

                        cursor.execute(
                            """
                            UPDATE users
                            SET password=%s
                            WHERE username=%s
                            """,
                            (
                                new_pass,
                                st.session_state["username"]
                            )
                        )

                        conn.commit()

                        st.success(
                            "Password Updated Successfully"
                        )

#for popup of confirmation of delete
@st.dialog("Delete Account")
def delete_popup():
    st.info(
        "Do you want to delete the account?\n"
        "If you click Confirm your account will be permanently deleted!"
    )
    if st.button("Confirm"):
        query = """
        DELETE FROM users
        WHERE username=%s
        """
        values = (
            st.session_state["username"],
        )
        cursor.execute(query, values)
        conn.commit()
        st.session_state.clear()
        st.success("Account deleted successfully.")
        st.switch_page("Home.py")
    if st.button("Cancel"):
        st.rerun()



if "username" not in st.session_state:
    st.warning("Please login or signin First!!")
    if st.button("Ok"):
        st.switch_page("Home.py") 

else:
    st.title("Welcome to User management System!!")
    st.text("Do you want to Update the username or Update the Password?")
    conn=connect_db()
    cursor=conn.cursor()
    if st.button("Update Account") :
        update_popup()
    if st.button("Delete Account"):
        delete_popup()
        
        
