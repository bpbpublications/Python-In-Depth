
import timeit

code_to_measure = ''' 
def func1(): 
    numbers = [] 
    for x in range(1000): 
        numbers.append(x*2 + x**2) 
'''

measure = timeit.timeit(stmt = code_to_measure,
                        number = 10000)
print("Execution time for function func1: ", measure)

print()

code_to_measure = ''' 
def func2(): 
    numbers = [x*2 + x**2 for x in range(1000)]     
'''

measure = timeit.timeit(stmt = code_to_measure,
                        number = 10000)
print("Execution time for function func2: ", measure)
