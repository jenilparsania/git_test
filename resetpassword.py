username = input("Enter username")
password = input("Enter pass: ")

if username == "admin" and password == "admin":
    print("you can reset")
else:
    print("you cannot reset")