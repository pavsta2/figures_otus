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

        if not isinstance(self.side_a, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_a)} instead')
        if not isinstance(self.side_b, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_b)} instead')
        if not isinstance(self.side_c, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_c)} instead')

        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError('Side cannot be equal and less then 0')

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
