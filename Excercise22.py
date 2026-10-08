#Contact book
m = {}
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View all")
    print("4. Exit")
    Choice = input("Choose: ")
    if Choice == "1":
        Name = input("Name: ")
        Phone = input("Phone: ")
        m[Name] = Phone
        print("Contact saved!")
    elif Choice == "2":
        Search_contact = input("Search Contact: ")
        if Search_contact in m:
            print("Contact found!")
            print("Name:", Search_contact)
            print("Phone:", m[Search_contact])
        else:
            print("Contact not found.")
    elif Choice == "3":
        for Contact, Number in m.items():
            print(Contact, ":", Number)
    elif Choice == "4":
        print("GoodBye!!!")
        break
    else:
        print("Invalid choice!")
