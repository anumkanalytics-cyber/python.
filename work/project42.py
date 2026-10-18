encrypt_pass = input("Enter your password: ")
dencrypt_pass = ""

for char in encrypt_pass.split():
    if char == "1!":
        dencrypt_pass = dencrypt_pass + "a"
    elif char == "2!":
        dencrypt_pass = dencrypt_pass + "b"
    elif char == "3!":
        dencrypt_pass = dencrypt_pass + "c"
    elif char == "4!":
        dencrypt_pass = dencrypt_pass + "d"
    elif char == "5!":
        dencrypt_pass = dencrypt_pass + "e"
    elif char == "6!":
        dencrypt_pass = dencrypt_pass + "f"
    elif char == "7!":
        dencrypt_pass = dencrypt_pass + "g"
    elif char == "8!":
        dencrypt_pass = dencrypt_pass + "h"
    elif char == "9!":
        dencrypt_pass = dencrypt_pass + "i"
    elif char == "10!":
        dencrypt_pass = dencrypt_pass + "j"
    elif char == "11!":
        dencrypt_pass = dencrypt_pass + "k"
    elif char == "12!":
        dencrypt_pass = dencrypt_pass + "l"
    elif char == "13!":
        dencrypt_pass = dencrypt_pass + "m"
    elif char == "14!":
        dencrypt_pass = dencrypt_pass + "n"
    elif char == "15!":
        dencrypt_pass = dencrypt_pass + "o"
    elif char == "16!":
        dencrypt_pass = dencrypt_pass + "p"
    elif char == "17!":
        dencrypt_pass = dencrypt_pass + "q"
    elif char == "18!":
        dencrypt_pass = dencrypt_pass + "r"
    elif char == "19!":
        dencrypt_pass = dencrypt_pass + "s"
    elif char == "20!":
        dencrypt_pass = dencrypt_pass + "t"
    elif char == "21!":
        dencrypt_pass = dencrypt_pass + "u"
    elif char == "22!":
        dencrypt_pass = dencrypt_pass + "v"
    elif char == "23!":
        dencrypt_pass = dencrypt_pass + "w"
    elif char == "24!":
        dencrypt_pass = dencrypt_pass + "x"
    elif char == "25!":
        dencrypt_pass = dencrypt_pass + "y"
    elif char == "26!":
        dencrypt_pass = dencrypt_pass + "z"
    else:
        dencrypt_pass = dencrypt_pass + "_NUM_OR_SPECIAL_CHAR_HERE_"

print("Decrypted password:", dencrypt_pass)
