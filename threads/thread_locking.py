import threading


class LockSwitch(threading.Thread):

    COUNT = None
    shared_resource_lock = None
    shared_resource_with_lock = 0
    shared_resource_with_no_lock = 0

    locked_switch = None
    locked_switches = 0
    unlocked_switch = None
    unlocked_switches = 0
    total_lock_count = {
        'increment_locked': 0,
        'decrement_locked': 0,
        'increment_unlocked': 0,
        'decrement_unlocked': 0,
    }

    def __init__(self, count):
        super().__init__()
        self.COUNT = count
        self.shared_resource_lock = self.shared_resource_lock or threading.Semaphore()

    def run(self):
        pass




def increment_with_lock():
    global shared_resource_with_lock
    global locked_switch
    global locked_switches
    for i in range(COUNT):
        shared_resource_lock.acquire()
        if locked_switch != 'increment':
            locked_switch = 'increment'
            locked_switches += 1
        shared_resource_with_lock += 1
        total_lock_count['increment_locked'] += 1
        # print(f"[increment] {shared_resource_with_lock}")
        shared_resource_lock.release()
    print(f"The value of shared variable with lock management is {shared_resource_with_lock}")
    print(f"The value of shared variable with race condition is {shared_resource_with_no_lock}")
    print(f"iwl_locked_switches: {locked_switches}")
    print(f"iwl_unlocked_switches: {unlocked_switches}")
    print("iwl_",total_lock_count)


def decrement_with_lock():
    global shared_resource_with_lock
    global locked_switch
    global locked_switches
    for i in range(COUNT):
        shared_resource_lock.acquire()
        if locked_switch != 'decrement':
            locked_switch = 'decrement'
            locked_switches += 1
        shared_resource_with_lock -= 1
        total_lock_count['decrement_locked'] += 1
        # print(f"[decrement] {shared_resource_with_lock}")
        shared_resource_lock.release()
    print(f"The value of shared variable with lock management is {shared_resource_with_lock}")
    print(f"The value of shared variable with race condition is {shared_resource_with_no_lock}")
    print(f"dwl_locked_switches: {locked_switches}")
    print(f"dwl_unlocked_switches: {unlocked_switches}")
    print("dwl_",total_lock_count)


def increment_without_lock():
    global shared_resource_with_no_lock
    global unlocked_switch
    global unlocked_switches
    for i in range(COUNT):
        if unlocked_switch != 'increment':
            unlocked_switch = 'increment'
            unlocked_switches += 1
        shared_resource_with_no_lock += 1
        total_lock_count['increment_unlocked'] += 1
    print(f"The value of shared variable with lock management is {shared_resource_with_lock}")
    print(f"The value of shared variable with race condition is {shared_resource_with_no_lock}")
    print(f"iwol_locked_switches: {locked_switches}")
    print(f"iwol_unlocked_switches: {unlocked_switches}")
    print("iwol_",total_lock_count)


def decrement_without_lock():
    global shared_resource_with_no_lock
    global unlocked_switch
    global unlocked_switches
    for i in range(COUNT):
        if unlocked_switch != 'decrement':
            unlocked_switch = 'decrement'
            unlocked_switches += 1
        shared_resource_with_no_lock -= 1
        total_lock_count['decrement_unlocked'] += 1
    print(f"The value of shared variable with lock management is {shared_resource_with_lock}")
    print(f"The value of shared variable with race condition is {shared_resource_with_no_lock}")
    print(f"dwol_locked_switches: {locked_switches}")
    print(f"dwol_unlocked_switches: {unlocked_switches}")
    print("dwol_",total_lock_count)


if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    print(f"The value of shared variable with lock management is {shared_resource_with_lock}")
    print(f"The value of shared variable with race condition is {shared_resource_with_no_lock}")
    print(f"locked_switches: {locked_switches}")
    print(f"unlocked_switches: {unlocked_switches}")
    print(total_lock_count)
