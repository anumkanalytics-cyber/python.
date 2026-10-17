def task_manager():
    print("----WELCOME TO TASK MANAGEMENT APP----")
    task = []

    total_task = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        task.append(task_name)

    print(f"Today's tasks are: {task}")

    while True:
        operation = int(input(f"Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\n"))

        if operation == 1:
            add = input("Enter task you want to add = ")
            task.append(add)
            print(f"Task '{add}' has been successfully added!")
        
        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")

            if updated_val in task:
                up = input("Enter new task = ")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'!")
            else:
                print("Task not found!")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")

            if del_val in task:
                task.remove(del_val)
                print(f"Task '{del_val}' has been deleted!")
            else:
                print("Task not found!")

        elif operation == 4:
            print(f"Total tasks = {len(task)}")
            print(f"Your tasks are: {task}")

        elif operation == 5:
            print("Closing the program... Goodbye!")
            break

        else:
            print("Invalid input! Please enter a number from 1 to 5.")

task_manager()