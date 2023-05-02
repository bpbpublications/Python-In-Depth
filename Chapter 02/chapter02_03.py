y = 0
x = input("Enter a value for Number: ")
x = int(x)

if x > 10:
    print("Number is greater than 10")
    y = x - 10
    print("Result of subtracting 10 from Number is:", y)
elif 0 < x < 10:
    print("Number is between 0 and 10")
    y = x + 10
    print("Result of adding 10 to Number is:", y)
elif x < 0:
    print("Number is negative")
else:
    print("Obviously, we have 0 or 10")
