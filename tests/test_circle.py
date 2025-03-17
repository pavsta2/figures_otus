"""Модуль тестов класса Circle"""
from math import pi
import pytest
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
def test_circle_creat_posit(type_of_data, get_data_circle_positive):
    """Позитивные тесты создания объектов Круга"""
    radius = get_data_circle_positive[type_of_data]
    try:
        Circle(radius)
    except ValueError as exc:
        assert False, f'Создание объекта круга с радиусом {radius} вызывает ошибку {exc}'


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
def test_circle_perimet_posit(type_of_data, get_data_circle_positive):
    """Позитивные проверки метода расчета периметра Круга"""
    radius = get_data_circle_positive[type_of_data]
    test_circle = Circle(radius)
    assert test_circle.perimeter == pi * radius * 2, 'Расчет периметра круга неверен'


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
def test_circle_area_posit(type_of_data, get_data_circle_positive):
    """Позитивные проверки метода расчета площади Круга"""
    radius = get_data_circle_positive[type_of_data]
    test_circle = Circle(radius)
    assert test_circle.area == pi * radius ** 2, 'Расчет площади круга неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             'str',
                             'bool',
                             'zero'
                          ],
                         ids=[
                             'str as radius',
                             'bool as radius',
                             'zeros as radius'
                         ])
def test_circle_creat_negot(type_of_data, get_data_circle_negotive):
    """Негативные проверки создания объектов Круга"""
    radius = get_data_circle_negotive[type_of_data]
    with pytest.raises(ValueError):
        Circle(radius)
