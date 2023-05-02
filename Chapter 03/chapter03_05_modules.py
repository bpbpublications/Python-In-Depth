LIMIT_NB = 10


def multiples_of_number(nb):
    """
        Print the numbers obtained by multiplying
        the input number by each number between 1 and LIMIT_NB.
    """
    n = 1
    while n < LIMIT_NB:
        print(n * nb)
        n = n + 1


def exponentials_of_number(nb):
    """
        Print the numbers obtained by calculating the exponential
        of the input number by each number between 1 and LIMIT_NB.
    """
    n = 1
    while n < LIMIT_NB:
        print(nb ** n)
        n = n + 1
