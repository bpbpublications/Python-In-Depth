############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of static method with decorator
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_adult = self.compare(self.age, 18)
        
    @staticmethod
    def compare(num1, num2):
        if num1 < num2:
            return False
        return True
