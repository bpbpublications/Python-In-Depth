############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of class method with decorator @classmethod
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    message = "Hello world!"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = True
        
    @classmethod
    def patient(cls, name, age, gender):
        cls.gender = gender
        cls.status = False
        print(cls.message)
        cls.message = "Sky line!"
        return cls(name, age)
