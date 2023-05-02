
numbers = []

for x in range(1000):
    y = x * 2 + x ** 2
    numbers.append(y)

res = sum(numbers)
print("Result:", res)