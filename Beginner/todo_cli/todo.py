import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i + 1}. {status} {task['task']}")

# Add a new task
def add_task(tasks):
    task_text = input("🆕 Enter a new task: ")
    tasks.append({"task": task_text, "done": False})
    save_tasks(tasks)
    print("Task added!")

# Mark a task as done
def mark_done(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        tasks[task_num]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['task']}")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

# Menu
def show_menu():
    print("""
🗓️ TO-DO LIST CLI
---------------------
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit
""")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye, Skhokho!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
