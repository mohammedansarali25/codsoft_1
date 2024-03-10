import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the task number to delete: "))
            delete_task(tasks, index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()