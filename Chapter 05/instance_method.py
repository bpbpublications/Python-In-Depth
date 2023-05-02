############################################################################################
#    Python in-depth
#    Chapter 5
#        Object Orientation
#
#    Example of instance method
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet( self ):
        print( "Hello, I’m {}.".format( self.name) )
