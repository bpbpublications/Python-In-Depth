############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of single inheritance
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet( self ):
        print( "Hello, I’m {}.".format( self.name) )
        

class Student(Person):
    def __init__( self, name, age, matr ):
        self.matr = matr
        super().__init__( name, age )
        