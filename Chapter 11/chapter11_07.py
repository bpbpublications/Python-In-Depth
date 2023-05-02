
import multiprocessing as mp
import time
import os


def exponentials_of_number(nb, q):
    limit = 10

    n = 1
    while n < limit:
        res = nb ** n
        q.put(res)
        n = n + 1

if __name__ == "__main__":
    q = mp.Queue()
    p = mp.Process(target=exponentials_of_number, args=(5, q))

    p.start()
    p.join()

    while not q.empty():
        print(q.get())
