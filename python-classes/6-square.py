#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """method to initiate"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """method to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to initalize value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """method to set position"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """method to return current square area"""
        return (self.__size**2)

    def my_print(self):
        """method to print stdout square with char #"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
