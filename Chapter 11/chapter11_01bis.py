
import threading

def add_one(x):
    print("Adding one to a number - Done in thread")
    print(x + 1)

print("1. We create a thread")
t = threading.Thread(target=add_one, args=(5,))
print(t)
print("2. We start the thread")
t.start()
