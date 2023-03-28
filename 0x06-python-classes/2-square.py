#!/usr/bin/python3
"Define a class Square"

class square:
    "represent a new Square"

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self._size = size
