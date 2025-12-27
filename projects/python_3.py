# simple login system  = checks the username and password
fixed_username = "Aashish"
fixed_password = "Aashish@12"

username = input("Enter the username:")
password = input("Enter the password:")

if username ==fixed_username and password == fixed_password:
    print("you signed up!")
else:
    print("Wrong username and password")