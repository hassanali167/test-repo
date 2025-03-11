"""
Topic: Decorators in Python

Explanation:
Decorators modify the behavior of functions or methods.
"""

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

"""
Code Explanation:
- `my_decorator()` takes a function as an argument.
- The wrapper function executes extra code before and after calling `func()`.
- `@my_decorator` applies the decorator to `say_hello()`.
"""
"""
Topic: Polymorphism in Python

Explanation:
Polymorphism allows the same method to have different behaviors in different classes.
"""

class Bird:
    def make_sound(self):
        return "Some generic bird sound"

class Parrot(Bird):
    def make_sound(self):
        return "Squawk!"

class Crow(Bird):
    def make_sound(self):
        return "Caw! Caw!"

# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Calling with different objects
parrot = Parrot()
crow = Crow()

animal_sound(parrot)
animal_sound(crow)

"""
Code Explanation:
- The parent class `Bird` defines a method `make_sound()`.
- Child classes `Parrot` and `Crow` override this method.
- The `animal_sound()` function demonstrates polymorphism.
"""
