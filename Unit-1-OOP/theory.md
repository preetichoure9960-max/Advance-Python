# OOP Basics:
OOP (Object-Oriented Programming): we create objects from classes

## Class
Blueprint of an object.

## Object
Instance of a class.

## Constructor 
Constructor runs automatically when an object is created.
~Special method called automatically.

## Instance Variable
Variable unique to each object.

## Instance Method
Methods that work with object data.
Example:
class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
s1 = Student("Preeti",101)
s1.display()


