

import threading
import time

def func(name, delay):
    print(f"    {name}: Start at {time.time()}")
    time.sleep(delay)
    print(f"    {name}: End at {time.time()}")

if __name__ == "__main__":
    DELAY = 2
    print(f"1. Main - Before: {threading.enumerate()}")

    t = threading.Thread(target=func, args=(f"Thread", DELAY,))
    t.start()

    print(f"2. While thread is running: {threading.enumerate()}")

    # wait a bit more than DELAY...
    time.sleep(DELAY + 2)
    print(f"3. Main - After: {threading.enumerate()}")
