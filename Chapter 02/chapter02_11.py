
input_numbers = range(1, 11)

for x in input_numbers:
    if x%10 == 0:
        raise ValueError("We do not allow multiples of 10")
    else:
        print("Got: ", x)



