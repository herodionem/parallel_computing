import multiprocessing
import time


def foo():
    print('Starting function')
    time.sleep(2)
    print('Finished "executing" function')


if __name__ == "__main__":
    p = multiprocessing.Process(target=foo)
    print('\nProcess before execution:', p, p.is_alive())
    print("Join then Terminate. Notice function dialogue and process exitcode...")
    p.start()
    print('Process running:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    p.terminate()
    print('Process terminated', p, p.is_alive())

    p = multiprocessing.Process(target=foo)
    print('\nProcess before execution:', p, p.is_alive())
    print("Terminate then Join. Notice function dialogue and process exitcode...")
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    # time.sleep(0.5)  # It takes some time for the process to shutdown. Without a bit of time between termination and next is_alive request, is_alive returns `True`
    print('Process terminated', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())

