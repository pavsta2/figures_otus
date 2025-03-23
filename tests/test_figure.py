"""Модуль проверки суперкласса Figure"""
import pytest
from src.square import Square
from src.circle import Circle


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             2,
                             2.5
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_add_area_posit(type_of_data):
    """Позитивные тесты метода суммирования площадей двух объектов фигур"""
    side_a = type_of_data
    test_square = Square(side_a)
    test_square_area = test_square.area
    radius = type_of_data
    test_circle = Circle(radius)
    test_circle_area = test_circle.area
    assert test_square.add_area(test_circle) == test_square_area + test_circle_area, \
        'Расчет суммы площадей двух фигур неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             2
                          ],
                         ids=[
                             'integers as sides'
                         ])
def test_add_area_negot(type_of_data):
    """Негативные проверки метода суммирования площадей двух объектов фигур"""
    side_a = type_of_data
    test_square = Square(side_a)
    with pytest.raises(ValueError):
        test_square.add_area(100)
