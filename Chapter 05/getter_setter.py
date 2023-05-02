############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of Getter/Setter
#
#    Author: Ahidjo Ayeva
###########################################################################################


class Person:
    def __init__( self, name, age ):
        self.name = name
        self.__age = age
        self.about = "I'm {}, {} years old.".format(self.name, self.__age)
        
    def get_age( self ):
        return self.__age
    
    def set_age( self, age ):
        self.__age = age
