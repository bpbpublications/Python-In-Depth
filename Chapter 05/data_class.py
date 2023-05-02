############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of Python Data Class
#
#    Author: Ahidjo Ayeva
###########################################################################################


from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    
    def __post_init__(self):
        self.name = self.name[0].upper() + self.name[1:].lower()
        
    def greet( self ):
        print( "Hello, I’m {}.".format( self.name) )
        
        
@dataclass
class Student(Person):
    matr: int