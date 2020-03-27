import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(f"Starting process with name: {name}")
    time.sleep(2)
    print(f"Exiting {name}")


if __name__ == "__main__":
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True
    no_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
    no_background_process.daemon = False
    background_process.start()
    no_background_process.start()
