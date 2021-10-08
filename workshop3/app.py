
from donation_pkg.homepage import show_homepage, donate, show_donations
from donation_pkg.user import login, register


database = {"admin": "password"}
donations = []
authorized_user = ""

if authorized_user == "":
    print("You must be logged in to donate\n")

else:
    print("Logged in as:", str(authorized_user))

while True:
    show_homepage()
    option = input("Choose an option: ")
    if option == "1" or option == "2":
        username = input("Enter Username:")

        password = input("Enter password:")
        username = username.lower()
    if option == "1":
        authorized_user = login(database, username, password)

    if option == "2":
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password

    if option == "3":

        if authorized_user == "":
            print("You are not loggeed in, please log in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    if option == "4":

        show_donations(donations)
    elif option == "5":
        print("Leaving DonateMe...")

        break
