from sheets import check_username

def register():
    """
    Asks users their username and checks if it exists or available
    """
    while True:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            print("Cancelled")
            break
        elif not username.isalpha():
            print("Username must contain only alphabetic characters")
        elif len(username.split(" "))>1:
            print("Username must not contain spaces")
        elif len(username)>15 or len(username)<5:
            print("Username length must be between 5 and 15 characters")
        elif check_username(username):
            print("Username already exists")
        else:
            print("Registration Successful")
            break
    
def login():
    """
    Asks users their username for logging in
    """
    while True:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            print("Cancelled")
            break
        elif check_username(username):
            print("Username already exists")
            break
        else:
            print("Wrong Username")

def start_option():
    """
    Asks users whether they want to login or register
    """
    print("\nHow would you like to proceed?\n")
    account_option = input("1 - Login\n2 - Register\nYour Input : ")
    if account_option == "1":
        login()
    elif account_option == "2":
        register()
    else:
        raise Exception("Invalid Input")
