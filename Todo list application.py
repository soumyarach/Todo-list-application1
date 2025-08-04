tasks = []

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        del tasks[task_number - 1]
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid input!")

load_tasks()

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")