import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(f"Starting process with name: {name}")
    time.sleep(2)
    print(f"Exiting {name}")

if __name__ == "__main__":
    process_with_name = multiprocessing.Process(name='the_foosa', target=foo)
    process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()