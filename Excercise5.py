#Temperature Converter
C = int(input("Enter Temperature in celsius: "))
F = (C * 9/5) + 32
if C < 10:
    print("your temperature is cold.")
elif C >= 25:
    print('Your temperature is Moderate.')
else:
    print("your temperature is Hot.")

