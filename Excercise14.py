#Number analyzer
how_many = int(input("How many numbers do you want to enter? "))
sum = 0
Largest = None
even_numbers = []
odd_numbers = []
for i in range(how_many):
    num = int(input("Enter a number: "))
    sum += num
    if Largest is None or num > Largest:
        Largest = num
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
Average = sum / how_many
print("Sum:", sum)
print("Average:", Average)
print("Largest:", Largest)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)