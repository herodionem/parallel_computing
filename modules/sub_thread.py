import threading
import time


class myThread(threading.Thread):

    kill_switch = 3
    thread_killer = None

    def __init__(self, threadID, name, counter):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}\n")
        print_time(self.name, self.counter, 5)
        print(f"Exiting {self.name}\n")



def print_time(threadName, counter, delay):
    while counter:
        if myThread.kill_switch <= 0:
            print(f"Kill switch {'was' if myThread.thread_killer else 'has been'} switched on {myThread.thread_killer or threading.currentThread().getName()}! "
                  f"{'All threads have been removed!' if myThread.thread_killer else ''}")
            myThread.thread_killer = threading.currentThread().getName()
            threading.currentThread()._delete()
        time.sleep(delay)
        print(f"testing {threading.currentThread().getName()}")
        print(f'{threadName}[{counter}]: {time.ctime(time.time())}')
        counter -= 1
        print(f"kill switch value: {myThread.kill_switch}")
        myThread.kill_switch -= 1


if __name__ == '__main__':
    thread1 = myThread(1, "Thread-1", 2)
    thread2 = myThread(2, "Thread-2", 4)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"\n\nmaster thread exiting.")