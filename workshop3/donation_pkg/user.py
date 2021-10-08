def login(database, username, password):

    if username in database and database[username] == password:

        print("Welcome back", username)
        return username
    elif username in database and database[username] != password:
        print("Incorrect password for ", username)
        return ""
    else:
        print(" user not found. Please register")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        print("Username has been registered")
        return username
