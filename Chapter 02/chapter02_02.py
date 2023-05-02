y = 0
x = input("Enter a value for Number: ")
x = int(x)

if x > 10:
    print("Number is greater than 10")
    y = x - 10
    print("Result of subtracting 10 from Number is:", y)
elif x < 0:
    print("Number is negative")
elif x < 10:
    print("Number is less than 10")
    y = x + 10
    print("Result of adding 10 to Number is:", y)
else:
    print("Number is equal to 10")
