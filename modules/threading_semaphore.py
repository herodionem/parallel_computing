"""
https://stackoverflow.com/questions/21736741/what-are-the-practical-uses-of-semaphores

"""

import threading
import time
import random


semaphore = threading.Semaphore(0)

item = None

class test(threading.Thread): ...

def consumer():
    global item
    print("consumer is waiting.")
    semaphore.acquire()
    print(f"[Consumer]: consumed item number {item}")
    time.sleep(1)


def producer():
    global item
    time.sleep(2)
    item = random.randint(0, 1000)
    print(f"[Producer]: produced item number {item}")
    time.sleep(0.5)
    semaphore.release()


if __name__ == '__main__':
    t1 = test(target=consumer)
    t2 = test(target=producer)
    # t1 = threading.Thread(target=consumer)
    # t2 = threading.Thread(target=producer)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print("master process terminating")
    time.sleep(2)
