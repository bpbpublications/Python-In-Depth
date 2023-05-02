############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of 'privat' attribute
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    
    def __init__( self, name, age ):
        self.name = name
        self.__age = age
        self.about = "I'm {}, {} years old.".format(self.name, self.__age)