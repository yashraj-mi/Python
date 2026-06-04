from task import Task

import time


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, func, interval=None, run_at=None):
        task = Task(func, interval=interval, run_at=run_at)
        self.tasks.append(task)
        print(f"Registered {task.name} at {time.strftime('%H:%M:%S')}")

    def run_pending(self):
        for task in self.tasks:
            if task.is_due():
                task.run()
