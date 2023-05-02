
import multiprocessing as mp
import time
import os


def exponentials_of_number(nb):
    limit = 10

    print(f"+++ Exponentials of {nb}:")

    process_id = os.getpid()
    print(f"Process {process_id}: Start at {time.time()}")

    n = 1
    while n < limit:
        print(nb ** n)
        n = n + 1

    print(f"Process {process_id}: End at {time.time()}")
    print()

if __name__ == "__main__":

    for n in [2, 5, 8]:
        p = mp.Process(target=exponentials_of_number, args=(n,))

        p.start()
        p.join()

    print("--- All done ---")
