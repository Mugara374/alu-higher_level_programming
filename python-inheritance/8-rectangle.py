#!/usr/bin/python3
# 8-rectangle.py
"""creates a subclass
Rectangle of parent
class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines
    a rectangle from
    BaseGeometry class
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
