#Password Attempt system
correct_password = "abc"
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Wrong password.")
if attempts == 3:
    print("Too many attempts. Access denied.")