from decoraters import every, at, scheduler
from runner import Runner
import time


@every(1)
def hello():
    print("Hello")


runner = Runner(scheduler)
runner.start()


@every(2)
def mango():
    print("Mango")


@at("12:30")
def token():
    print("token")


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    runner.stop()
    print("Scheduler Stopped!")
