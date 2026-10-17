#Movie ticket system
age = int(input("Enter your age, please: "))
day = input("Enter your day: ")
num_ticket = int(input("Enter number of tickets: "))

if age > 13:
    price = 300
elif age >= 5:
    price = 200
else:
    price = 600

if day == "Saturday" or day == "Sunday":
    price = price + 100

subtotal = price * num_ticket

if day == "Wednesday":
    discount = subtotal * 20 / 100
else:
    discount = 0

final_total = subtotal - discount

print("Ticket price: Rs.", price)
print("Quantity:", num_ticket)
print("Subtotal: Rs.", subtotal)
print("Wednesday discount: Rs.", int(discount))
print("Final total: Rs.", int(final_total))