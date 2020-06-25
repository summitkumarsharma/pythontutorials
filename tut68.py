# Abstract Base Class & @abstractmethod

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod   # we can import in this way also


# class Shape(metaclass=ABCMeta):
class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "rectangle"
    no_of_sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth


rect = Rectangle()
print(rect.print_area())

# tryObj = Shape()  we can not create object of Abstract Class
