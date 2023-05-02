############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of static method with function
#
#    Author: Ahidjo Ayeva
###########################################################################################

def compare(num1, num2):
        if num1 < num2:
            return False
        return True
    
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_adult = self.compare(self.age, 18)
        
    compare = staticmethod(compare)
    
