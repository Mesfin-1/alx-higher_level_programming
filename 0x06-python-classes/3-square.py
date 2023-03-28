#!/usr/bin/python3
"Define a class Square"

def _init_(self, size=0):
    "Initialize a new square"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self._size = size

    def area(self)
    "return the current area of square"
    return (self._size * self._size)
