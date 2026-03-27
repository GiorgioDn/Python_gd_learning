# verification user
verify_user = ["admin", "12345"]

# list that will contain user data
entry_user = []

# username request
username = input("Enter username: ")
entry_user.append(username)

# password request
password = input("Enter password: ")
entry_user.append(password)

# check if username and password are correct
if entry_user[0] == verify_user[0] and entry_user[1] == verify_user[1]:
    print("Welcome")
    secret = []

    answer = input("What is your favorite animal: ")
    secret.append(answer)
else:
    print("Wrong credentials")
