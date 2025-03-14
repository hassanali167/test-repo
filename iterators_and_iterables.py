"""
Topic: Iterators and Iterables in Python

Explanation:
An iterable is an object that can return an iterator (e.g., lists, tuples).
An iterator implements `__iter__()` and `__next__()`.
"""

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Returns an iterator object

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Using the iterator
counter = Counter(1, 5)
for num in counter:
    print(num)

"""
Code Explanation:
- `Counter` class implements an iterator.
- `__next__()` method returns the next value.
- `StopIteration` is raised when the sequence ends.
"""
