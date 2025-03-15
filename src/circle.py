"""Это модуль класса круга"""
from math import pi
from figure import Figure


class Circle(Figure):
    """
    Класс для создания объектов типа круг
    """
    def __init__(self, radius: (int, float)) -> None:
        self.radius = radius

        if not isinstance(self.radius, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.radius)} instead')

        if self.radius <= 0:
            raise ValueError('Radius cannot be equal and less then 0')

    @property
    def perimeter(self) -> int | float:
        return pi * self.radius * 2

    @property
    def area(self) -> int | float:
        return pi * self.radius ** 2
