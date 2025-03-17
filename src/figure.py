"""Это модуль базового класса фигуры"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Супер класс для создания классов типа фигура
    """

    @property
    @abstractmethod
    def area(self):
        """Метод для расчета площади фигуры"""

    @property
    @abstractmethod
    def perimeter(self):
        """Метод для расчета периметра фигуры"""

    def add_area(self, figure) -> int | float:
        """Метод для суммирования площади фигуры с площадью другой фигуры"""
        if not isinstance(figure, Figure):
            raise ValueError(f'Type of argument "figure" must be "Figure", '
                             f'got {type(figure)} instead')
        return self.area + figure.area

    @staticmethod
    def check_type(*args):
        """Метод для проверки типа данных, передаваемого в качестве стороны фигуры"""
        for arg in args:
            if not isinstance(arg, int | float) or isinstance(arg, bool):
                raise ValueError(f'Side must be int or float, got {type(arg)} instead')

    @staticmethod
    def check_is_positive_num(*args):
        """Метод для проверки положительности числа, передаваемого в качестве стороны фигуры"""
        for arg in args:
            if arg <= 0:
                raise ValueError('Figure argument cannot be equal and less then 0')
