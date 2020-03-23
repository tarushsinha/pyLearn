## Object Oriented Programming (OOP)

## Paradigms of Programming previously covered:
## -> imperative programming (using statements, loops, functions as subroutines, etc.)
## -> functional programming (using pure functions, higher-order functions, recursion)


## Object-Oriented Programming is another popular paradigm of programming
## Objects are created using classes, which are the focal point of OOP

## Classes define what the object will be, but is separate from the object itself (classes are blueprints)
## Classes are created using the keyword `class`, and contains methods of the class.
## Default initializations of all instances of the class (objects) go in the def __init__(): method

class Cat:
    def __init__(self, name, breed, color, legs):
        self.name = name
        self.breed = breed
        self.color = color
        self.legs = legs

    def identify(self):
        print(
            "Hi my name is {0}, I am a {1} {2} cat with {3} legs".format(self.name, self.color, self.breed, self.legs))

def tag(Cat):
    print(
        "Hi my name is {0}, I am a {1} {2} cat with {3} legs - and I've been tagged".format(
            Cat.name, Cat.color, Cat.breed, Cat.legs))

MJ = Cat("MJ", "Tabby", "Brown", 4)
Kovu = Cat("Kovu", "Tabby", "Black", 4)
Stumpy = Cat("Stumpy", "Siamese", "White", 3)

## __init__(self): Constructor
## Most important method in a class - instances of a class have attributes - pieces of data associated with them
## referenced by self.attributes

MJ.identify()
Kovu.identify()
tag(Stumpy)

## Methods
## --> Add functionality to the class
## --> All methods must have self as their first parameter

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("\"Woof\" - {0}".format(self.name))


Luna = Dog("Luna", "Golden")
Luna.bark()

## Class attributes - by creating & assigning variables within the body of the class, they can be accessed by all Obj's

class Bird:
    wings = 2
    legs = 2
    beak = 1

    def __init__(self, name):
        self.name = name

    def identify(self):
        print(
            "Hi my name is {0}, I have {1} wings and {2} legs".format(self.name, self.wings, self.legs))

Beakman = Bird("Beakman")
Beakman.identify()

## Python doesn't support multiple constructors, so we can pass default values instead

class Flamingo:
    def __init__(self, name, wings = 2, legs = 2):
        self.name = name
        self.wings = wings
        self.legs = legs

    def identify(self):
        print(
            "Hi my name is {0}, I have {1} wings and {2} legs".format(self.name, self.wings, self.legs))

Pink = Flamingo("Pink")
Pink.identify()

Gaga = Flamingo("Gaga", 1)
Gaga.identify()

## Inheritance -- Provides a way to share functionality between classes
## To inherit methods from the "superclass", imagine the following:

class Vehicle:
    def __init__(self, name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color



class Car(Vehicle):
    def __init__(self, name, engine, color, wheels, doors):
        self.wheels = wheels
        self.doors = doors

        Vehicle.__init__(self, name, engine, color)

class Plane(Vehicle):
    def __init__(self, name, engine, color, wheels, wings, doors):
        self.wheels = wheels
        self.wings = wings
        self.doors = doors

        Vehicle.__init__(self, name, engine, color)

Boeing = Plane("Boeing", "large", "white", 8, 4, 6)
Mazda = Car("Mazda", "small", "black", 4, 2)

print(Boeing.__dict__)
print(Mazda.__dict__)

## A class that inherits from another class is called a subclass
## A class that is inherited from is called a superclass
## If a class inherits from another with the same attributes or methods it overides them

class Lion:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        print("Roar")

class Cat(Lion):
    def __init__(self, name, color, breed):
        self.breed = breed
        Lion.__init__(self,name,color)

    def speak(self):
        print("Meow")

Marilyn = Cat("Marilyn", "Brown", "Tabby")
Marilyn.speak()

## the `super` function is an inheritance-related function that refers to the parents class
## this function can be used to find the method with a certain name in an object's superclass

class Primate():
    def __init__(self, name, strenth):
        self.name = name
        self.strength = strenth

    def adrenaline(self):
        print(self.strength * 2)

class Human(Primate):
    def __init__(self, name, strength):
        Primate.__init__(self, name, strength)

    def danger(self):
        super().adrenaline()

Joe = Human("Joe", 5)
Joe.danger()

## Data Hiding - Encapsulation which involves packaging of related variables & functions into a single object

## Static methods defined by @staticmethod

## Properties can be set by defining setter/getter functions

