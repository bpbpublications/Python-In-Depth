
import profile

LIMIT_NB = 1000


def exponentials(nb):
    """
        List the numbers obtained by calculating the exponential
        of the input number by each number between 1 and LIMIT_NB.
    """
    n = 1
    res = []
    while n < LIMIT_NB:
        res.append(nb ** n)
        n = n + 1
    return res

def exponentials_for_seq(seq):
    res =  []
    for x in seq:
        res = res + exponentials(x)
    return res

profile.run('exponentials_for_seq(range(1, 10))')