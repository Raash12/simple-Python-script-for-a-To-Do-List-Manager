# todo.py

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    """Main function to run the To-Do List Manager."""
    tasks = []
    
    print("Welcome to the To-Do List Manager!")
    print("\nFeatures:")
    print("1. Add Task: Allows the user to add a new task to the list.")
    print("2. View Tasks: Displays all the current tasks.")
    print("3. Delete Task: Lets the user remove a specified task by number.")
    print("4. Exit: Exits the application.")
    
    while True:
        print("\nTo-Do List Manager")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        
        elif choice == '2':
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()