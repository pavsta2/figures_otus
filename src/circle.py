"""Это модуль класса круга"""
from math import pi
from src.figure import Figure


class Circle(Figure):
    """
    Класс для создания объектов типа круг
    """
    def __init__(self, radius: (int, float)) -> None:
        self.radius = radius

        self.check_type(self.radius)
        self.check_is_positive_num(self.radius)

    @property
    def perimeter(self) -> int | float:
        return pi * self.radius * 2

    @property
    def area(self) -> int | float:
        return pi * self.radius ** 2
