#Shopping cart  
cart = []
while True:
    print("1. View cart")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Your cart:", cart)
    elif choice == "2":
        item = input("Enter item: ")
        cart.append(item)
        print("Added!")
    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Removed!")
        else:
            print("Item not found!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        continue