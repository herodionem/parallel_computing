import multiprocessing

def function(i):
    print(f'called function in process: {i}')
    return


if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        process_jobs.append(i)
        p.start()
        p.join()