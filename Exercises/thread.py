# Create a thread that prints numbers from 1 to 10.
import threading
def task():
    for i in range(10):
        print(i)

t1 = threading.Thread(target=task)
t1.start()

t1.join()


# Use multiprocessing to run two functions in parallel.
# Measure execution time of a function using time module.

from multiprocessing import Process
import time


def sum(n=50000000):
    sum = 0
    for i in range(n + 1):
        sum += i
    print(sum)


start = time.time()
p1 = Process(target=sum, args=(50000000,))
p2 = Process(target=sum, args=(50000000,))

p1.start()
p2.start()

p1.join()
p2.join()


print(p1, p2)
print("Multiprocessing Time:", time.time() - start)

start2 = time.time()
sum(50000000)
sum(50000000)
print("Normal Time:", time.time() - start2)


