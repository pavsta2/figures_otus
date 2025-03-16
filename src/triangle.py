"""Это модуль класса треугольника"""
from math import sqrt
from figure import Figure


class Triangle(Figure):
    """
    Класс для создания объектов типа треугольник
    """
    def __init__(self, side_a: (int | float), side_b: (int | float), side_c: (int | float)) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        self.check_type(self.side_a)
        self.check_type(self.side_b)
        self.check_type(self.side_c)

        self.check_is_positive_num(side_a)
        self.check_is_positive_num(side_b)
        self.check_is_positive_num(side_c)

        if not ((self.side_a + self.side_b) > self.side_c and
                (self.side_b + self.side_c) > self.side_a and
                (self.side_a + self.side_c) > self.side_b):
            raise ValueError('Triangle inequalities rule is violated')

    @property
    def perimeter(self) -> int | float:
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self) -> int | float:
        return sqrt(self.perimeter/2 * (self.perimeter/2 - self.side_a) *
                    (self.perimeter/2 - self.side_b) *
                    (self.perimeter/2 - self.side_c))
