#Restauant ordering system
foods = {
    "1": "Pizza",
    "2": "Shawarma",
    "3": "Cheesy sticks",
    "4": "French fries",
    "5": "Chicken burger"
}
prices = {
    "1": 2000,
    "2": 500,
    "3": 200,
    "4": 500,
    "5": 600
}
orders = []
while True:
    print("1. Show Menu")
    print("2. Order Item")
    print("3. View Order")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        for number in foods:
            print(number, foods[number], "-", prices[number])
    elif choice == "2":
        item = input("Enter item number: ")
        quantity = int(input("Enter quantity: "))
        order = (foods[item], quantity)
        orders.append(order)
        print("Item added!")
    elif choice == "3":
        print("Your Order:")
        for item, quantity in orders:
            print(item, "x", quantity)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")