from task_manager import TaskManager


def show_menu():
    print("\n===== Student Task Manager =====")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def handle_add(manager):
    title = input("Enter task title: ")
    try:
        task = manager.add_task(title)
        print(f"Task added: {task}")
    except ValueError as error:
        print(f"Error: {error}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager):
    task_id = int(input("Enter task ID to complete: "))
    manager.complete_task(task_id)
    print("Task marked as completed.")


def handle_delete(manager):
    task_id = int(input("Enter task ID to delete: "))
    manager.delete_task(task_id)
    print("Task deleted.")


def main():
    manager = TaskManager()
    actions = {
        "1": handle_add,
        "2": handle_display,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()