
import multiprocessing as mp
import time
import os

def func(delay):
    process_id = os.getpid()
    print(f"Process {process_id}: Start at {time.time()}")
    time.sleep(delay)
    print(f"Process {process_id}: End at {time.time()}")
    print()

if __name__ == "__main__":

    for x in [2, 5]:
        p = mp.Process(target=func, args=(x,), daemon=True)
        p.start()

    print("--- All done ---")
