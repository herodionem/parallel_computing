from threading import Thread, Condition
import time

items = [1,2,3,4,5,6,7,8,9,10]
condition = Condition()

class consumer(Thread):
    def __init__(self):
        super().__init__()

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print(f"{time.ctime(time.time())}\t[Consumer]: no item to consume")
        items.pop()
        print(f"{time.ctime(time.time())}\t[Consumer]: consumed 1 item")
        print(f"{time.ctime(time.time())}\t[Consumer]: {len(items)} items to consume")
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 18):
            time.sleep(1/3)
            print(f"{time.ctime(time.time())}\tCONSUMER {i}")
            self.consume()


class producer(Thread):
    def __init__(self):
        super().__init__()

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            print(f"{time.ctime(time.time())}\t[producer]: shared resource full")
            condition.wait()
        items.append(1)
        print(f"{time.ctime(time.time())}\t[producer]: {len(items)} items produced")
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(1)
            print(f"{time.ctime(time.time())}\tPRODUCER {i}")
            self.produce()


if __name__ == "__main__":
        producer = producer()
        consumer = consumer()
        producer.start()
        consumer.start()
        producer.join()
        consumer.join()
