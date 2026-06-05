import threading
import time
from queue import Queue


def worker(name: str) -> None:
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


def thread_demo() -> None:
    print("\n===== Basic Threads =====")

    thread_1 = threading.Thread(target=worker, args=("A",))
    thread_2 = threading.Thread(target=worker, args=("B",))
    thread_3 = threading.Thread(target=worker, args=("C",))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()

    print("All threads finished")


def counter_demo() -> None:
    print("\n===== Lock Example =====")

    counter = 0
    lock = threading.Lock()

    def increment() -> None:
        nonlocal counter

        for _ in range(100_000):
            with lock:
                counter += 1

    thread_1 = threading.Thread(target=increment)
    thread_2 = threading.Thread(target=increment)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Counter:", counter)


class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount: int) -> None:
        with self.lock:
            self.balance += amount

    def withdraw(self, amount: int) -> None:
        with self.lock:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance")

    def check_balance(self) -> int:
        with self.lock:
            return self.balance


def bank_account_demo() -> None:
    print("\n===== Bank Account =====")

    account = BankAccount(500)

    thread_1 = threading.Thread(target=account.deposit, args=(1000,))
    thread_2 = threading.Thread(target=account.deposit, args=(500,))
    thread_3 = threading.Thread(target=account.withdraw, args=(500,))
    thread_4 = threading.Thread(target=account.withdraw, args=(1500,))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    print("Final Balance:", account.check_balance())


class CarParking:
    def __init__(self, total_slots: int):
        self.total_slots = total_slots
        self.semaphore = threading.BoundedSemaphore(total_slots)
        self.lock = threading.Lock()
        self.current_parked = 0

    def park_car(self, car_name: str, parking_time: int) -> None:
        print(
            f"{time.strftime('%H:%M:%S')} | "
            f"{car_name} waiting for parking..."
        )

        with self.semaphore:
            with self.lock:
                self.current_parked += 1
                print(
                    f"{time.strftime('%H:%M:%S')} | "
                    f"{car_name} parked "
                    f"({self.current_parked}/{self.total_slots})"
                )

            time.sleep(parking_time)

            with self.lock:
                self.current_parked -= 1
                print(
                    f"{time.strftime('%H:%M:%S')} | "
                    f"{car_name} left "
                    f"({self.current_parked}/{self.total_slots})"
                )


def car_parking_demo() -> None:
    print("\n===== Car Parking =====")

    parking_lot = CarParking(4)

    cars = [
        ("Car A", 3),
        ("Car B", 2),
        ("Car C", 4),
        ("Car D", 1),
        ("Car E", 2),
        ("Car F", 3),
    ]

    threads = []

    for car_name, parking_time in cars:
        thread = threading.Thread(
            target=parking_lot.park_car,
            args=(car_name, parking_time),
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Parking simulation completed")


def producer_consumer_demo() -> None:
    print("\n===== Producer Consumer =====")

    task_queue = Queue(maxsize=50)

    def producer() -> None:
        for task_id in range(20):
            task_queue.put(task_id)

        for _ in range(3):
            task_queue.put(None)

    def consumer() -> None:
        while True:
            task = task_queue.get()

            if task is None:
                task_queue.task_done()
                break

            time.sleep(1)
            print(f"Task {task} completed")

            task_queue.task_done()

    producer_thread = threading.Thread(target=producer)

    consumers = [
        threading.Thread(target=consumer)
        for _ in range(3)
    ]

    producer_thread.start()

    for thread in consumers:
        thread.start()

    producer_thread.join()

    task_queue.join()

    for thread in consumers:
        thread.join()

    print("All tasks completed")


def main() -> None:
    thread_demo()
    counter_demo()
    bank_account_demo()
    car_parking_demo()
    producer_consumer_demo()


if __name__ == "__main__":
    main()