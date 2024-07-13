#!/usr/bin/python3
""" Square definition in script """


class Square:
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        if 'height' in kwargs and 'width' in kwargs:
            height = kwargs['height']
            width = kwargs['width']

            if not isinstance(height, (int, float)):
                raise TypeError("height must be int or float")
            if not isinstance(width, (int, float)):
                raise TypeError("height must be int or float")
            if height < 0:
                raise ValueError("height must be >= 0")
            if width < 0:
                raise ValueError("height must be >= 0")
            if height != width:
                raise ValueError("height and width must be equal")

            self.height = height
            self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        return self.height * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    try:
        s = Square(width=12, height=-8)
        print(s)
        print(s.area_of_my_square())
        print(s.permiter_of_my_square())
    except (TypeError, ValueError) as e:
        print(e)
