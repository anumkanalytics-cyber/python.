student_grades = {}
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not found!")


def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")


def display_all_students():
    if student_grades:
        print("\n--- All Students ---")
        for name, grade in student_grades.items():
            print(f"Name: {name} | Grade: {grade}")
    else:
        print("No students found or added.")


def main():
    while True:
        print("\n--- Student Grades Management System ---")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5!")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty!")
                continue

            try:
                grade = int(input("Enter student grade: "))
                if not 0 <= grade <= 100:
                    print("Grade must be between 0 and 100!")
                    continue
                add_student(name, grade)
            except ValueError:
                print("Please enter a valid numeric grade!")

        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter new grade: "))
                if not 0 <= grade <= 100:
                    print("Grade must be between 0 and 100!")
                    continue
                update_student(name, grade)
            except ValueError:
                print("Please enter a valid numeric grade!")

        elif choice == 3:
            name = input("Enter student name: ").strip()
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()