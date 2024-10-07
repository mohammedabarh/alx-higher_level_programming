#!/usr/bin/python3
"""Defines a class Box."""


class Box:
    """
    Class that defines properties of a box: (based on 2-rectangle.py).

    Attributes:
        length (int): length of the box.
        breadth (int): breadth of the box.
    """
    
    def __init__(self, length=0, breadth=0):
        """Creates new instances of Box.

        Args:
            length (int, optional): length of the box. Defaults to 0.
            breadth (int, optional): breadth of the box. Defaults to 0.
        """
        self.breadth = breadth
        self.length = length

    @property
    def length(self):
        """Length retriever.

        Returns:
            int: the length of the box.
        """
        return self.__length

    @property
    def breadth(self):
        """Breadth retriever.

        Returns:
            int: the breadth of the box.
        """
        return self.__breadth

    @length.setter
    def length(self, value):
        """Property setter for length of box.

        Args:
            value (int): length of the box.

        Raises:
            TypeError: if length is not an integer.
            ValueError: if length is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("length must be an integer")
        elif value < 0:
            raise ValueError("length must be >= 0")
        else:
            self.__length = value

    @breadth.setter
    def breadth(self, value):
        """Property setter for breadth of box.

        Args:
            value (int): breadth of the box.

        Raises:
            TypeError: if breadth is not an integer.
            ValueError: if breadth is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("breadth must be an integer")
        elif value < 0:
            raise ValueError("breadth must be >= 0")
        else:
            self.__breadth = value

    def area(self):
        """Calculates area of a box.

        Returns:
            int: area.
        """
        return self.__breadth * self.__length

    def perimeter(self):
        """Calculates perimeter of a box.

        Returns:
            int: perimeter.
        """
        if self.__breadth == 0 or self.length == 0:
            return 0
        else:
            return 2 * (self.__breadth + self.__length)

    def __str__(self):
        """Prints the box with the character #.

        Returns:
            str: the box.
        """
        box_representation = []

        if self.__length == 0 or self.__breadth == 0:
            return ""

        for i in range(self.__breadth):
            for j in range(self.__length):
                box_representation.append("#")
            box_representation.append("\n")

        # remove blank line
        box_representation.pop()

        return "".join(box_representation)
