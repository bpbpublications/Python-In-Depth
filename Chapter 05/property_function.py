############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of Python property using @property function
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    
    def about(self):
        return '{}, {} years old.'.format(self.name, self.age)
    
    def __get_age( self ):
        return self.__age
    
    def __set_age( self, value ):
        self.__age = value
    
    about = property(about)
    age = property(__get_age, __set_age)