"""
Topic: Collections Module in Python

Explanation:
The `collections` module provides specialized data structures like namedtuple, deque, Counter, and defaultdict.
"""

from collections import namedtuple, deque, Counter, defaultdict

# Named tuple
Person = namedtuple("Person", "name age")
p = Person("Alice", 25)
print("NamedTuple:", p.name, p.age)

# Deque (double-ended queue)
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print("Deque:", d)

# Counter (counts elements in a list)
counter = Counter("mississippi")
print("Counter:", counter)

# Defaultdict (provides default values for missing keys)
dd = defaultdict(int)
dd["a"] += 1
print("Defaultdict:", dd)

"""
Code Explanation:
- `namedtuple()` creates an immutable object with named fields.
- `deque` allows fast append/pop from both ends.
- `Counter` counts occurrences of elements.
- `defaultdict` assigns default values if a key doesn't exist.
"""
