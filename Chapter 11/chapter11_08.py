
import multiprocessing as mp
import time


def exponentials_of_number(nb):
    limit = 10
    res = []

    n = 1
    while n < limit:
        res.append(nb ** n)
        n = n + 1
    return res


if __name__ == '__main__':
    numbers = [2, 4, 6]
    pool = mp.Pool(processes=3)
    work_result = pool.map(exponentials_of_number, numbers)
    for i in work_result:
        print(i)
