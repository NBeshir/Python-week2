import donation_pkg


def show_homepage():

    print("\n === DonateMe Homepage ===")
    print("------------------------------------------")
    print("\n| 1.    Login     | 2.    Register     |")
    print("------------------------------------------")

    print("\n| 3.    Donate    | 4.    Show Donations       |")
    print("\n|                | 5.    Exit      |")

    print("------------------------------------------")


def donate(username):

    donation_amt = input("Enter amount to donate:")

    #donation_amt_float = float(donation_amt)
    donation = username, "donated $", donation_amt

    print("Thank you for your donation!")

    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    total = 0
    if donations:
        for donation in donations:

            print(donation)
            total = total + donation
            print("Total =$", total)
    else:
        print("Currently, there are no donations.")
