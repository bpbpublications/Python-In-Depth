############################################################################################
#    Python in-depth
#
#    Chapter 5
#
#        Object Orientation
#
#    Example of Python Abstract Base Class (ABC)
#
#    Author: Ahidjo Ayeva
###########################################################################################


from abc import ABCMeta, abstractmethod


class ABC_Person(metaclass=ABCMeta):
    @abstractmethod
    def greet():
        pass
    
    @property
    @abstractmethod
    def about(self):
        return ""
    
    @property
    @abstractmethod
    def age(self):
        pass
    
    @age.setter
    @abstractmethod
    def age(self):
        return
    

class Person(ABC_Person):
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    @property
    def about(self):
        return "I'm {}, {} years old.".format(self.name, self.age)
    
    def greet(self):
        return "Hello, I'm {}!".format(self.name)
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
        
class Student(Person):
    def __init__(self, name, age, matr):
        self.matr = matr
        super().__init__(name, age)