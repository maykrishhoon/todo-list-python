from datetime import datetime

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show all tasks with status
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task.startswith("✔ ") else "[ ]"
            print(f"{i}. {status} {task.replace('✔ ', '')}")

# Add new task with timestamp
def add_task(task, tasks):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    task_with_time = f"{task} (Added on {timestamp})"
    tasks.append(task_with_time)
    save_tasks(tasks)

# Delete a task
def delete_task(index, tasks):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

# Mark a task as complete
def complete_task(index, tasks):
    if 0 <= index < len(tasks):
        tasks[index] = "✔ " + tasks[index].replace("✔ ", "")
        save_tasks(tasks)
        print("Marked as complete.")
    else:
        print("Invalid task number.")

# Edit an existing task
def edit_task(index, new_task, tasks):
    if 0 <= index < len(tasks):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks[index] = f"{new_task} (Edited on {timestamp})"
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Main menu system
def main():
    tasks = load_tasks()
    while True:
        print("\n📝 To-Do List Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Edit Task")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task, tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(index, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to edit: ")) - 1
                new_task = input("Enter the new task: ")
                edit_task(index, new_task, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
