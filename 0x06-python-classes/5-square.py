#!/usr/bin/python3
"Define a class square"
class Square:
    "represent a new square"
    @property
    def size(self):
        "get the current size of square"
        return (self._size)
    @size.setter
    def size(self, value):
        if not isinstance(vale, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = value

        def area(self):
            "return the current srea of the square"
            return (self._size *self._size)

        def my_print(self):
            "print square with #"
            for j in range(0, self._size):
                [print("#", end="") for k in range(self._size)]
                print("")
             if self._size == 0:
                    print("")
