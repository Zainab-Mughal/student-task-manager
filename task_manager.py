"""Core logic for the Student Task Manager."""


class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.completed = True
        return task

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            raise ValueError(f"No task found with ID {task_id}.")
        self.tasks.remove(task)
        return task
