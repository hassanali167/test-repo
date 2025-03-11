"""
Topic: Inheritance in Python

Explanation:
Inheritance allows a class (child) to inherit properties and methods from another class (parent).
"""

# Parent class
class Animal:
    def speak(self):
        return "I make sounds"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Creating instances
animal = Animal()
dog = Dog()

print("Animal:", animal.speak())
print("Dog:", dog.speak())

"""
Code Explanation:
- The `Animal` class has a method `speak()`.
- `Dog` class inherits from `Animal` and overrides `speak()`.
- Objects of both classes demonstrate method overriding.
"""
