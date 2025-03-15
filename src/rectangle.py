"""Это модуль класса прямоугольника"""
from figure import Figure


class Rectangle(Figure):
    """
    Класс для создания объектов типа прямоугольник
    """
    def __init__(self, side_a: (int, float), side_b: (int, float)) -> None:
        self.side_a = side_a
        self.side_b = side_b

        if not isinstance(self.side_a, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_a)} instead')
        if not isinstance(self.side_b, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_b)} instead')

        if self.side_a <= 0 or self.side_b <= 0:
            raise ValueError('Side cannot be equal and less then 0')

    @property
    def perimeter(self) -> int | float:
        return (self.side_a + self.side_b) * 2

    @property
    def area(self) -> int | float:
        return self.side_a * self.side_b
