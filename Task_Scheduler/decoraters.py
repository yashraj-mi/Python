from scheduler import Scheduler

scheduler = Scheduler()


def every(seconds):
    def decorater(func):
        scheduler.add_task(func, interval=seconds)
        return func

    return decorater


def at(time_str):
    def decorater(func):
        scheduler.add_task(func, run_at=time_str)
        return func

    return decorater
