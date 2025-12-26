"""
Topic: Classes and Objects in Python

Explanation:
Python supports Object-Oriented Programming (OOP) with classes and objects.
A class is a blueprint for creating objects.
"""


# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 25)

# Calling a method
print(person1.greet())

"""
Code Explanation:
- The `Person` class has an `__init__` method to initialize attributes.
- The `greet()` method returns a formatted string.
- An object `person1` is created, and the `greet()` method is called.
"""
