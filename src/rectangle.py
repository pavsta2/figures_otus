"""Это модуль класса прямоугольника"""
from figure import Figure


class Rectangle(Figure):
    """
    Класс для создания объектов типа прямоугольник
    """
    def __init__(self, side_a: (int, float), side_b: (int, float)) -> None:
        self.side_a = side_a
        self.side_b = side_b

        self.check_type(self.side_a)
        self.check_type(self.side_b)

        self.check_is_positive_num(self.side_a)
        self.check_is_positive_num(self.side_b)

    @property
    def perimeter(self) -> int | float:
        return (self.side_a + self.side_b) * 2

    @property
    def area(self) -> int | float:
        return self.side_a * self.side_b
