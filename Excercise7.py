u = input("Enter your username: ")
p = input("Enter your Password: ")
Correct_u = str("admin")
Correct_p = str("python123")
if u == Correct_u and p == Correct_p:
    print("Login successful! Wellcome admin!")
else:
    print("Incorrect password or username, please try again.")