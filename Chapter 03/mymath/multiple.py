
def multiples_of_number(nb, limit=10):
    """
        Print the numbers obtained by multiplying
        the input number by each number between 1 and the limit number.
    """
    n = 1
    while n < limit:
        print(n * nb)
        n = n + 1

