############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of class method with function classcmethod()
#
#    Author: Ahidjo Ayeva
###########################################################################################


def patient(cls, name, age, gender):
    cls.gender = gender
    cls.status = False
    print(cls.message)
    cls.message = "Sky line!"
    return cls(name, age)

class Person:
    
    message = "Hello world!"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = True
        
    patient = classmethod(patient)