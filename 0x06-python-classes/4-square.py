#!/usr/bin/python3
"Define a square"

class Square:
    "represent a square"
    def _init_(self, size=0):
        "initialize a new square"
        self._size = size

    @property
    def size(self, value):
        if not isinstance(vale, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

        def area(self):
            "return the current area of the square"
            return (self._size * self._size)
