"""Модуль проверки суперкласса Figure"""
import pytest
from src.square import Square
from src.circle import Circle


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             'integer',
                             'float'
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_add_area_posit(type_of_data, get_data_square_positive, get_data_circle_positive):
    """Позитивные тесты метода суммирования площадей двух объектов фигур"""
    side_a = get_data_square_positive[type_of_data]
    test_square = Square(side_a)
    test_square_area = test_square.area
    radius = get_data_circle_positive[type_of_data]
    test_circle = Circle(radius)
    test_circle_area = test_circle.area
    assert test_square.add_area(test_circle) == test_square_area + test_circle_area, \
        'Расчет суммы площадей двух фигур неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             'integer'
                          ],
                         ids=[
                             'integers as sides'
                         ])
def test_add_area_negot(type_of_data, get_data_square_positive):
    """Негативные проверки метода суммирования площадей двух объектов фигур"""
    side_a = get_data_square_positive[type_of_data]
    test_square = Square(side_a)
    with pytest.raises(ValueError):
        test_square.add_area(100)
