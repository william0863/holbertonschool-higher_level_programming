#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Method to initiate"""
        self.__size = size

    @property
    def size(self):
        """method to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """method to return current square area"""
        return (self.__size**2)

    def my_print(self):
        """method to print stdout square with char #"""
        if self.__size is 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print('{}'.format('#'), end="")
            print()
