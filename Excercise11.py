#Number guessing game
print("Correct! you got it!")
num = int(input("Guess a number: "))

while num != 50:
    if num > 50:
        print("Too high!")
    elif num < 50:
        print("Too low!")
    
    num = int(input("Guess again: "))

print("Correct! You got it!")