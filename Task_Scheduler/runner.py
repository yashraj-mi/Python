import threading
import time


class Runner:

    def __init__(self, scheduler, check_interval=1):
        self.scheduler = scheduler
        self.check_interval = check_interval
        self.running = False
        self.thread = None

    def _loop(self):
        while self.running:
            self.scheduler.run_pending()
            time.sleep(self.check_interval)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
