
import timeit


LIMIT_NB = 10


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


SETUP_CODE = '''
from __main__ import LIMIT_NB, exponentials
from random import randint
'''

code_to_measure = ''' 
nb = randint(1, 10) 
exponentials(nb)
'''

measure = timeit.timeit(setup = SETUP_CODE,
                        stmt = code_to_measure,
                        number = 10000)
print("Measure: ", measure)
