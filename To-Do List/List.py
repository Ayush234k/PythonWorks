def display_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your list.")

def remove_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your list.")
    else:
        print("Invalid task number.")

def todo_list():
    tasks = []
    while True:
        print("To-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

todo_list()
