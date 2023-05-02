
def exponentials_of_number(nb, limit=10):
    """
        Print the numbers obtained by calculating the exponential
        of the input number by each number between 1 and the limit number.
    """
    n = 1
    while n < limit:
        print(nb ** n)
        n = n + 1
