tasks = []
userChoice = True

while userChoice:
    print("\n1 for add task")
    print("2 for remove task")
    print("3 for printing all tasks")
    print("4 to exit")

    def addTask():
        tasks.append(input("Enter Task: "))

    def removeTask():
        try:
            temp = int(input("Which task number to remove: "))
            if 1 <= temp <= len(tasks):
                tasks.pop(temp - 1)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        except IndexError:
            print("Task number out of range.")

    def viewAllTasks():
        if tasks:
            print("\nYour tasks:\n")
            for count, task in enumerate(tasks, start=1):
                print(f"{count}: {task}")
        else:
            print("\nNo tasks available.")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            removeTask()
        elif choice == 3:
            viewAllTasks()
        elif choice == 4:
            userChoice = False
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Please enter a valid number.")
