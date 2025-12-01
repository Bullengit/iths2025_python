
password = "passkey123"
login_attempts = 0


username = input("Username: ")

while True:
     
    if len(username) <1:
        print ("Invalid username!")
        username = input("New attempt. Username: ")
        continue

    if login_attempts >= 5:
        print("Too many attempts, contact admin.")
        break      
    password_failure = input("Password: ")

    if len(password_failure) <8 or password_failure != password:
        print ("Password is incorrect, try again.")
        login_attempts = login_attempts + 1
        continue
    print("Correct credentials, you're logged in.")
    break
