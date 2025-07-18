def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip().split("|") for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task, status in tasks:
            file.write(f"{task}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        for i, (task, done) in enumerate(tasks, 1):
            print(f"{i}. {task} [{'Done' if done == '1' else 'Pending'}]")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append([task, "0"])

def mark_done(tasks):
    show_tasks(tasks)
    num = input("Task number to mark done: ")
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        tasks[int(num)-1][1] = "1"

def delete_task(tasks):
    show_tasks(tasks)
    num = input("Task number to delete: ")
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        tasks.pop(int(num)-1)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View  2. Add  3. Done  4. Delete  5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
