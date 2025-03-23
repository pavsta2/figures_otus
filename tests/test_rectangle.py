"""Модуль тестов класса Rectangle"""
import pytest
from src.rectangle import Rectangle


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 2],
                             [2.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_rectangle_creat_posit(type_of_data):
    """Позитивные тесты создания объектов Прямоугольника"""
    side_a, side_b = type_of_data
    assert Rectangle(side_a, side_b)


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 2],
                             [2.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_rectangle_perimet_posit(type_of_data):
    """Позитивные тесты метода расчета периметра Прямоугольника"""
    side_a, side_b = type_of_data
    test_rectangle = Rectangle(side_a, side_b)
    assert test_rectangle.perimeter == (side_a + side_b) * 2, ('Расчет периметра прямоугольника '
                                                               'неверен')


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 2],
                             [2.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_rectangle_area_posit(type_of_data):
    """Позитивные тесты метода расчета площади Прямоугольника"""
    side_a, side_b = type_of_data
    test_rectangle = Rectangle(side_a, side_b)
    assert test_rectangle.area == side_a * side_b, 'Расчет площади прямоугольника неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             ['1', '2'],
                             [True, True],
                             [0, 0]
                          ],
                         ids=[
                             'str as sides',
                             'bool as sides',
                             'zeros as sides'
                         ])
def test_rectangle_creat_negot(type_of_data):
    """Негативные тесты создания объектов Прямоугольника"""
    side_a, side_b = type_of_data
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
