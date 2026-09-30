#mini calculator
x = int(input("Enter number: "))
y = input("Enter operator (+, -, *, /): ")
z = int(input("Enter second number: "))

if y == "/" and z == 0:
    print("Error")
elif y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Invalid operator.")