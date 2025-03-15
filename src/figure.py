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
