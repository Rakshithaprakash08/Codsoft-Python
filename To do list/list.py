def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete/Incomplete")
    print("6. Exit")
    choice = input("Choose an option: ")
    return choice

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{idx}. {task['task']} - {status}")

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task details: ")
        tasks[task_num - 1]["task"] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
        status = "Complete" if tasks[task_num - 1]["completed"] else "Incomplete"
        print(f"Task marked as {status}.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        choice = display_menu()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task(tasks)
        elif choice == "6":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()