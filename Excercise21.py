# Student database
students = {
    "student1": {
        "name": "Ali",
        "age": 15,
        "marks": 85,
        "grade": "A"
    },
    "student2": {
        "name": "Sara",
        "age": 16,
        "marks": 78,
        "grade": "B"
    },
    "student_3": {
        "name": "Ahmad",
        "age": 17,
        "marks": 95,
        "grade": "A1"
    }
}
for student in students:
    print("Name:", students[student]["name"])
    print("Age:", students[student]["age"])
    print("Marks:", students[student]["marks"])
    print("Grade:", students[student]["grade"])
    print()
search_name = input("Enter student name: ")
found = False
for student in students:
    if students[student]["name"] == search_name:
        print("Name:", students[student]["name"])
        print("Age:", students[student]["age"])
        print("Marks:", students[student]["marks"])
        print("Grade:", students[student]["grade"])
        found = True
        break
if found == False:
    print("Student not found")