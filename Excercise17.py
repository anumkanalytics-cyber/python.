#To do list
tasks = ["Study Python", "Do homework", "Go shopping", "Clean room"]
task = input("Enter the task you want to search for: ")
if task in tasks:
    print("Task found!")
else:
    print("Task not found.")