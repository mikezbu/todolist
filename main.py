tasks = []

def addTask():
    task = input("Enter Task: ")
    task.append(task)
    print(f"Task '{task}' is added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")

    print("Here are the tasks: ")
    for task in tasks:
        print(task)

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # of the task you want to delete:"))

        if taskToDelete >= 0 and taskToDelete > len(tasks):
            tasks.pop(tasktoDelete)
            print(f"The task number '{taskToDelete} has been deleted.")
    
        else:
            print(f"The task number '{taskToDelete} is not in the list.")

    except:
        print("Invalid input.")


if __name__ == "__main__":
    print("Welcome to the to do list app :)")

    while True:
        print("\n")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice")

        if(choice == "1"):
            print("You have chosen: Add a Task")
            addTask()
            
        elif(choice == "2"):
            print("You have chosen: Delete a Task")
            deleteTask()

        elif(choice == "3"):
            print("You have chosen: List Tasks")
            listTasks()

        elif(choice == "4"):
            print("You have chosen: Quit")
            break

        else:    
            print("Invalid input, please enter a valid input.")

        print("Thanks for choosing this")
