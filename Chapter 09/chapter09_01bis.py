
import time

numbers = []

start = time.time()

for x in range(1000):
    y = x * 2 + x ** 2
    numbers.append(y)

end = time.time()

t = end - start
print("Loop execution time:", t)

res = sum(numbers)
print("Result:", res)