"""Это модуль класса квадрата"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Класс для создания объектов типа квадрат
    """
    def __init__(self, side_a: (int, float)) -> None:
        super().__init__(side_a, side_a)
        if not isinstance(self.side_a, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_a)} instead')
        if not isinstance(self.side_b, int | float):
            raise ValueError(f'Side must be int or float, got {type(self.side_b)} instead')
        if self.side_a <= 0:
            raise ValueError('Side cannot be equal and less then 0')
