# OBJECT ORIENTED PROGRAMMING
r"""
ABSTRACTION
*Abstract representation of a system

*A type of an abstraction is a class.

*Encapsulation is hiding the internal state and functionality of an object and
only allowing access through a public set of functions

*Inheritance: allows us to define a class that inherits all the data attributes 
and methods from another class.

*Polymorphism: ability to implement inherited properties or
 methods in different ways across multiple abstractions.For example:
 cat and tiger have mutual methods but also separate methods. 
 We can create our own versions of inherited methods.

 Class Animal(object):                        <= Inheritance
    <define attributions here>

Class Cat(Animal):
    def__init__(self,age):   <-this is a constructor Encapsulation(instance method)
        self.age = age                           magic method(__name__)
        self.name= None                         we hide the state of an onject inside a data class

Jelly = Cat(4)
"""


class Animal(object):
    def __init__(self, age):  # magic method
        self.age = age
        self.name = None

    def speak(self):  # instance method
        print(f'I am an animal. My name is {self.name}.')

    def __str__(self):
        return f'Animal name: {self.name}, age: {self.age}'


class Cat(Animal):
    def speak(self):
        print(f'I am a cat. My name is {self.name}. Meow')

    def __str__(self):
        return f'cat name: {self.name},age: {self.age}'


animec = Animal(10)
animec.name = "Animec"
animec.age = 12
animec.speak()
print(animec)  # this works because animals have a defined magic method string

anima = Animal(18)
anima.name = "ANIMA"
print(anima)

billy = Cat(12)
billy.name = "Billy"
billy.speak()
print(billy)

johny = Cat(18)
johny.name = "johny"
johny.speak()
print(johny)
