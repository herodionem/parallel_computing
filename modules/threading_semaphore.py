import threading
import time
import random


semaphore = threading.Semaphore(0)


def consumer():
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
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("master process terminating")
    time.sleep(2)
