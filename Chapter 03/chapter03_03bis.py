def multiples_of_number(nb):
    """
        Print the numbers obtained by multiplying
        the input number by each number between 1 and 20.
    """
    n = 1
    while n < 20:
        print(n * nb)
        n = n + 1

print(help(multiples_of_number))
