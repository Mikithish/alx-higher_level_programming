#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    pass



#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
