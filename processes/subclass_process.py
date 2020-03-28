import multiprocessing


class TestProcess(multiprocessing.Process):

    def run(self):
        print(f"Called run method in {self.name}")
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = TestProcess()
        jobs.append(p)
        p.start()
        p.join()
