import json
from datetime import datetime

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✔️" if task['completed'] else "❌"
            priority = f"[{task['priority']}]"
            due_date = f"(Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{idx}. {status} {priority} {task['title']} {due_date}")

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def main():
    """Main function to run the To-Do List Manager."""
    tasks = load_tasks()
    
    print("Welcome to the To-Do List Manager!")
    print("\nFeatures:")
    print("1. Add Task: Allows the user to add a new task to the list.")
    print("2. View Tasks: Displays all the current tasks.")
    print("3. Delete Task: Lets the user remove a specified task by number.")
    print("4. Complete Task: Mark a task as completed.")
    print("5. Set Due Date: Assign a due date to a task.")
    print("6. Exit: Exits the application.")
    
    while True:
        print("\nTo-Do List Manager")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task_title = input("Enter the task: ")
            priority = input("Enter priority (low, medium, high): ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            task = {
                'title': task_title,
                'completed': False,
                'priority': priority,
                'due_date': due_date if due_date else None
            }
            tasks.append(task)
            save_tasks(tasks)
            print(f"Task '{task_title}' added.")
        
        elif choice == '2':
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed_task['title']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to complete: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]['completed'] = True
                    save_tasks(tasks)
                    print(f"Task '{tasks[task_number - 1]['title']}' marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to set a due date: "))
                if 1 <= task_number <= len(tasks):
                    due_date = input("Enter due date (YYYY-MM-DD): ")
                    tasks[task_number - 1]['due_date'] = due_date
                    save_tasks(tasks)
                    print(f"Due date for task '{tasks[task_number - 1]['title']}' set to {due_date}.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()