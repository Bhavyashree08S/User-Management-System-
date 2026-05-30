import re
def valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&*!_+-]", password):
        return False
    return True

def valid_username(username):

    if len(username) < 5:
        return False

    return True