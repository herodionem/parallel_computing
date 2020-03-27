from threading import Thread
import string
import random


class threads_object(Thread):
    def run(self):
        function_to_run()


class nothreads_object(object):
    def run(self):
        function_to_run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
        for i in funcs:
            i.run()
# def function_to_run():
#     pass

def function_to_run():
    a,b = 0,1
    for i in range(10000):
        a,b = b,a+b

# def function_to_run():
#     k = open('test_read.txt', 'r').read()

# def function_to_run():
#     i = string.ascii_lowercase
#     s = [random.choice(i) for _ in range(10000)]
#     del s


def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))


if __name__ == "__main__":
    import sys
    from timeit import Timer

    repeat = 100
    number = 1
    num_threads = [1,2,4,8]

    print("Starting tests")
    for i in num_threads:
        t = Timer(f"non_threaded({i})", "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results(f"non_threaded({i} iters)", best_result)

        t = Timer(f"threaded({i})", "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results(f"threaded({i} threads)", best_result)

    print('Iterations Complete')
