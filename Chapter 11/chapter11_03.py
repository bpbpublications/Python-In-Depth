
import threading
import time

def func(name, delay):
    print(f"    {name}: Start at {time.time()}")
    time.sleep(delay)
    print(f"    {name}: End at {time.time()}")

if __name__ == "__main__":

    for n, x in enumerate([2, 5], start=1):
        print("--->")
        print(f"Before creating thread {n}")
        t = threading.Thread(target=func, args=(f"Thread-{n}", x,))
        print(f"Before running thread {n}")
        t.start()
        print(f"Wait for the thread {n} to finish")
        t.join()

    print("--->")
    print("All done")
