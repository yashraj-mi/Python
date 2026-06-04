import time


class Task:
    def __init__(self, func, interval=None, run_at=None):
        self.func = func
        self.interval = interval
        self.run_at = run_at
        self.last_run = None
        self.name = func.__name__

    def is_due(self):

        now = time.time()

        if self.interval:
            if self.last_run is None:
                return True
            return (now - self.last_run) >= self.interval

        if self.run_at:
            current_time = time.strftime("%H:%M")
            if current_time == self.run_at:
                if self.last_run is None:
                    return True

                return (now - self.last_run) >= 60

        return False

    def run(self):
        print(f"Running {self.name} at {time.strftime('%H:%M:%S')}")
        self.func()
        self.last_run = time.time()
