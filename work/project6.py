#Student management system
menu = {
    "1": "Add Student",
    "2": "View Students",
    "3": "Search Student",
    "4": "Calculate Class Average",
    "5": "Show Top Student",
    "6": "Show Passed Students",
    "7": "Show Failed Students",
    "8": "Exit"
}
students = []
unique_names = set()
def add_student():
    name = input("Enter student name: ")
    if name in unique_names:
        print("Student already exists!")
        return
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "grade": grade
    }
    students.append(student)
    unique_names.add(name)
    print("Student added successfully!")
def view_students():
    if len(students) == 0:
        print("No students found!")
        return
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])
        print()
def search_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            print("Student found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            return
    print("Student not found!")
def calculate_average():
    if len(students) == 0:
        print("No students found!")
        return
    total = 0
    for student in students:
        total += student["marks"]
    average = total / len(students)
    print("Class Average:", average)
def show_top_student():
    if len(students) == 0:
        print("No students found!")
        return
    top_student = students[0]
    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student
    summary = (
        top_student["name"],
        top_student["marks"],
        top_student["grade"]
    )
    print("Top Student:", summary)
def show_passed_students():
    print("Passed Students:")
    for student in students:
        if student["marks"] >= 50:
            print(student["name"])
def show_failed_students():
    print("Failed Students:")
    for student in students:
        if student["marks"] < 50:
            print(student["name"])
while True:
    for number, option in menu.items():
        print(number, option)
    choice = input("Choose: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        show_top_student()
    elif choice == "6":
        show_passed_students()
    elif choice == "7":
        show_failed_students()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")