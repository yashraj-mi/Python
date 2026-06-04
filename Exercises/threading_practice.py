import threading
import time

# def worker(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")

# t1 = threading.Thread(target=worker, args=("A",))
# t2 = threading.Thread(target=worker, args=("B",))
# t3 = threading.Thread(target=worker, args=("C",))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("All Done")

# counter=0
# lock=threading.Lock()

# lock.acquire()
# lock.release()


# def increment():
#     global counter
#     for  _ in range(150000000):
#         # lock.acquire()
#         with lock:

#             counter+=1
#         # lock.release()


# t1=threading.Thread(target=increment)
# t2=threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(counter)


# class BankAccount:

#     def __init__(self, amount):
#         self.balance = amount
#         self.lock = threading.Lock()

#     def deposit(self, amount):
#         with self.lock:
#             self.balance += amount

#     def withdraw(self, amount):
#         with self.lock:

#             if amount <= self.balance:

#                 self.balance -= amount
#             else:
#                 print("Insufficient Balance")

#     def check_balance(self):
#         with self.lock:
#             return self.balance


# a1 = BankAccount(500)


# t1 = threading.Thread(target=a1.deposit, args=(1000,))
# t2 = threading.Thread(target=a1.deposit, args=(500,))
# t4 = threading.Thread(target=a1.withdraw, args=(1500,))
# t3 = threading.Thread(target=a1.withdraw, args=(500,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# print(a1.check_balance())


# ====================================================================================================

# class CarParking:

#     def __init__(self, slots):
#         self.parking_slots = slots
#         self.sem = threading.BoundedSemaphore(self.parking_slots)
#         self.lock = threading.Lock()
#         self.current_parked = 0

#     def park_car(self, car_name, parking_time):
#         try:

#             print(f"{time.strftime('%H:%M:%S')} | {car_name} waiting for parking...")

#             with self.sem:

#                 with self.lock:
#                     self.current_parked += 1
#                     print(
#                         f"{time.strftime('%H:%M:%S')} {car_name} is parked / Occupacy: {self.current_parked}/{self.parking_slots}"
#                     )

#                 time.sleep(parking_time)

#                 with self.lock:
#                     self.current_parked -= 1
#                     print(
#                         f"{time.strftime('%H:%M:%S')} {car_name} is out from  parking / Occupacy: {self.current_parked}/{self.parking_slots}"
#                     )
#         except Exception as e:
#             print(f"Exception  Occured with {car_name}: {e}")


# p1 = CarParking(4)

# threads = []

# cars = [
#     ("Car A", 12),
#     ("Car B", 3),
#     ("Car C", 7),
#     ("Car D", 2),
#     ("Car E", 9),
#     ("Car F", 1),
#     ("Car G", 5),
#     ("Car H", 11),
#     ("Car I", 4),
#     ("Car J", 8),
#     ("Car K", 2),
#     ("Car L", 6),
#     ("Car M", 10),
#     ("Car N", 1),
#     ("Car O", 3),
# ]


# for car, delay in cars:
#     t = threading.Thread(target=p1.park_car, args=(car, delay))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()


# ==========================================================================


from queue import Queue

q = Queue(50)


def producer():
    for i in range(20):
        q.put(i)
        
    for _ in range(3):
        q.put(None)

def consumer():
    while True:
        
        job=q.get()
        if job is None:
            q.task_done()
            break
        
        time.sleep(1)
        print(f"{job} task is completed")
        q.task_done()

        

p1=threading.Thread(target=producer)
c1=threading.Thread(target=consumer)
c2=threading.Thread(target=consumer)
c3=threading.Thread(target=consumer)
p1.start()
c1.start()
c2.start()
c3.start()
p1.join()
q.join()
c1.join()
c2.join()
c3.join()

print("All task done")
    
#===================================================================================



