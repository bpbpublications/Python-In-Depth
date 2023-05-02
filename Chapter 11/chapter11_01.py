
import threading

def add_one(x):
    print("Adding one to a number - Done in thread")
    print(x + 1)

print("We create a thread")
t = threading.Thread(target=add_one, args=(5,))
print(t)
