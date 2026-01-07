def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks in your list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def todo_list():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        display_tasks(tasks)
        print("\nOptions: add / remove / quit")
        choice = input("Enter your choice: ").lower()

        if choice == "add":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added!")
        elif choice == "remove":
            if not tasks:
                print("Your task list is empty.")
                continue
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "quit":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid option. Choose add, remove, or quit.")

if __name__ == "__main__":
    todo_list()
