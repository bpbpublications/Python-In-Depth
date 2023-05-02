############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of Python property using @property decorator
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    @property
    def about(self):
        return '{}, {} years old.'.format(self.name, self.age)
    
    @property
    def age( self ):
        return self.__age
    
    @age.setter
    def age( self, value ):
        self.__age = value
        