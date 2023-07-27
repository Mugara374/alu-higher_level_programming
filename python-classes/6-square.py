#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size(int): length of side of the square.
            position(int tuple): position of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Properties for the length of a side of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for private attribute size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """setter function for private attribute position."""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints square with char #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        """String representation constructor of this square."""
        square_str = ""
        if self.__size == 0:
            return square_str
        for _ in range(self.__position[1]):
            square_str += "\n"
        for _ in range(self.__size):
            square_str += "{}{}\n".format(" " * self.__position[0], "#" * self.__size)
        return square_str.strip()
