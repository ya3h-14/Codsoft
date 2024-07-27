class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = 'Pending'
            print(f"Task '{task}' added.")
        else:
            print(f"Task '{task}' already exists.")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            print(f"Task '{task}' updated to '{status}'.")
        else:
            print(f"Task '{task}' does not exist.")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' does not exist.")

    def view_tasks(self):
        if self.tasks:
            for task, status in self.tasks.items():
                print(f"Task: {task} - Status: {status}")
        else:
            print("No tasks found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to update: ")
            status = input("Enter the new status (Pending/Completed): ")
            todo_list.update_task(task, status)
        elif choice == '3':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
