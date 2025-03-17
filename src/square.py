"""Это модуль класса квадрата"""
from src.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс для создания объектов типа квадрат
    """
    def __init__(self, side_a: (int, float)) -> None:
        self.check_type(side_a)
        self.check_is_positive_num(side_a)
        super().__init__(side_a, side_a)
