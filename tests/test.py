"""Write a few unittests."""

import unittest


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width
        """_summary_
        """

    def set_height(self, height):
        self.height = height


class TestGetArea(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")


unittest.main()
