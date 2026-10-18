user_pass = input("Enter your password: ")
encrpt_pass = ""
for char in user_pass:
    if char == "1":
        encrpt_pass += "a"
    elif char == "2":
        encrpt_pass += "b"
    elif char == "3":
        encrpt_pass += "c"
    elif char == "4":
        encrpt_pass += "d"
    elif char == "5":
        encrpt_pass += "e"
    elif char == "6":
        encrpt_pass += "f"
    elif char == "7":
        encrpt_pass += "g"
    elif char == "8":
        encrpt_pass += "h"
    elif char == "9":
        encrpt_pass += "i"
    elif char == "0":
        encrpt_pass += "j"
    else:
        encrpt_pass += "_NUM_OR_SPECIAL_CHAR_HERE_"

print("Encrypted password:", encrpt_pass)
