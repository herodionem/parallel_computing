import threading
import time


def fn_1():
    print(threading.currentThread().getName() + str(' is preening... \n'))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' has finished its ablutions and is exiting \n'))
    return

def fn_2():
    print(threading.currentThread().getName() + str(' is preening... \n'))
    time.sleep(3)
    print(threading.currentThread().getName() + str(' has finished its ablutions and is exiting \n'))
    return

def fn_3():
    print(threading.currentThread().getName() + str(' is preening... \n'))
    time.sleep(6)
    print(threading.currentThread().getName() + str(' has finished its ablutions and is exiting \n'))
    return


if __name__ == '__main__':
    t1 = threading.Thread(name='fn_1', target=fn_1)
    t2 = threading.Thread(name='fn_2', target=fn_2)
    t3 = threading.Thread(name='fn_3', target=fn_3)

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()

    print("The calling thread is terminating...\n")
