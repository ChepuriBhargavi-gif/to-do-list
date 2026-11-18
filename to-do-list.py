class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
         self.tasks.append({"task": task, "completed": False})
         print("Task added successfully!")
    def remove_task(self, task):
         for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print("Task removed successfully!")
                return
         print("Task not found in the list.")

    def mark_completed(self, task):
         for t in self.tasks:
             if t["task"] == task:
                 t["completed"] = True
                 print("Task marked as completed!")
                 return
         print("Task not found in the list.")

    def display_tasks(self):
         if self.tasks:
             print("Tasks:")
             for i, t in enumerate(self.tasks, start=1):
                 status = "Completed" if t["completed"] else "Not Completed"
                 print(f"{i}. {t['task']} - {status}")
         else:
             print("No tasks in the list.")

def main():
     todo_list = TodoList()
    
     while True:
         print("\nTODO LIST MENU:")
         print("1. Add a task")
         print("2. Remove a task")
         print("3. Mark a task as completed")
         print("4. Display tasks")
         print("5. Exit")

         choice = input("Enter your choice (1/2/3/4/5): ")

         if choice == '1':
             task = input("Enter task to add: ")
             todo_list.add_task(task)
         elif choice == '2':
             task = input("Enter task to remove: ")
             todo_list.remove_task(task)
         elif choice == '3':
             task = input("Enter task to mark as completed: ")
             todo_list.mark_completed(task)
         elif choice == '4':
             todo_list.display_tasks()
         elif choice == '5':
             print("Exiting...")
             break
         else:
             print("Invalid choice. Please enter a valid option.")
main()




import csv
import os


class TodoList:

    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename

        self.load_tasks()

    def add_task(self, task):
        if not task.strip():
            print("Task cannot be empty!")
            return

        self.tasks.append({
            "task": task,
            "completed": False
        })

        print("Task added successfully!")
        self.save_tasks()

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"].lower() == task.lower():
                self.tasks.remove(t)
                print("Task removed successfully!")
                self.save_tasks()
                return

        print("Task not found in the list.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"].lower() == task.lower():
                if t["completed"]:
                    print("Task is already completed!")
                else:
                    t["completed"] = True
                    print("Task marked as completed!")
                    self.save_tasks()
                return

        print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print("\nYOUR TODO LIST:")

            for i, t in enumerate(self.tasks, start=1):

                status = (
                    "Completed"
                    if t["completed"]
                    else "Not Completed"
                )

                print(f"{i}. {t['task']} - {status}")

        else:
            print("No tasks in the list.")

    def save_tasks(self):
        try:
            with open(
                self.filename,
                mode="w",
                newline="",
                encoding="utf-8"
            ) as file:

                fieldnames = ["task", "completed"]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(self.tasks)

            print("Tasks saved automatically!")

        except OSError as error:
            print(f"Error saving tasks: {error}")

    def load_tasks(self):
        if not os.path.exists(self.filename):
            print("No saved tasks found. Starting fresh!")
            return

        try:
            with open(
                self.filename,
                mode="r",
                newline="",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:
                    if (
                        "task" in row
                        and "completed" in row
                        and row["task"] is not None
                    ):
                        self.tasks.append({
                            "task": row["task"],
                            "completed": (
                                row["completed"].strip().lower()
                                == "true"
                            )
                        })

            print("Tasks loaded successfully!")

        except (OSError, csv.Error) as error:
            print(f"Error loading tasks: {error}")


def main():

    todo_list = TodoList()

    while True:

        print("------- TODO LIST MENU --------")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display tasks")
        print("5. Save tasks")
        print("6. Exit")
        print("---------------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":

            task = input("Enter task to add: ")
            todo_list.add_task(task)

        elif choice == "2":

            task = input("Enter task to remove: ")
            todo_list.remove_task(task)

        elif choice == "3":

            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)

        elif choice == "4":

            todo_list.display_tasks()

        elif choice == "5":

            todo_list.save_tasks()

        elif choice == "6":

            todo_list.save_tasks()
            print("Tasks saved. Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


main()