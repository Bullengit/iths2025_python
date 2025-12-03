user_credentials = {"user1": "Welcome123", "user2": "qwerty!", "user3": "Password2025"}

password_list = ["123456", "password", "Welcome123", "letmein", "Password2025"]

for user in user_credentials.items():
    current_user = user[0]
    user1_pass = user[1]
    for password in password_list:
        if user1_pass ==password:
            print(f"{current_user}:{password} -> Successful")
            file = open("matching_cred.txt", "a")
            file.write(f"{current_user}:{password} -> Successful\n")
            file.close()
        else:
            print(f"{current_user}:{password} -> Failed")
            file = open("matching_cred.txt", "a")
            file.write(f"{current_user}:{password} -> Failed\n")
            file.close()

        #Alternativt
        successOrFailedText = "Failed"
        if user1_pass == password:
            successOrFailedText = "Successful"

        print(f"{current_user}:{password} -> {successOrFailedText}")
        file = open("matching_cred.txt", "a")
        file.write(f"{current_user}:{password} -> {successOrFailedText}\n")
        file.close()