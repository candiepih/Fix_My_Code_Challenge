#!/usr/bin/python3
"""Class Square
Defines a squaare geometry
"""


class Square:
    """Defines square geometry
    Attributes:
        width (int): the width of the square
        height (int): the height of the square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes the Square class
        Args:
            args: arguments passed on instance
            kwargs: keyword arguments passes on instance
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ String representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
