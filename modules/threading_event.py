import time
from threading import Thread, Event
import random

items = []
event = Event()

class consumer(Thread):
    def __init__(self, items, event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(0.5)
            print(f"{self.name} ", self.items)
            print(f"{self.name} Waiting...")
            self.event.wait()
            item = self.items.pop()
            print(f"Consumer notify: {item} popped from list by {self.name}")


class producer(Thread):
    def __init__(self, integers, event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            item = int(i)
            self.items.append(item)
            print(f"Producer notify: item {item} appended to list by {self.name}")
            print(f"Producer notify: event set by {self.name}")
            self.event.set()
            print(f"Producer notify: event cleared by {self.name}")
            self.event.clear()
        print(f"{self.name} ", self.items)


if __name__ == "__main__":
    t1 = producer(items, event)
    t2 = consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
