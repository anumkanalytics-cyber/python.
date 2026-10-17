Age = int(input("Enter your age: "))

if Age >= 18:
    print("you are an adult")
    print("you can vote")
elif Age <= 18:
    print("you are in school")
    print("you cannot vote")
else:
    print("you are a kid")
print("Thank you")