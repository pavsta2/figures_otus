"""Модуль тестов класса Circle"""
from math import pi
import pytest
from src.circle import Circle


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             2,
                             2.5
                          ],
                         ids=[
                             'integers as radius',
                             'floats as radius'
                         ])
def test_circle_creat_posit(type_of_data):
    """Позитивные тесты создания объектов Круга"""
    radius = type_of_data
    assert Circle(radius)


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             2,
                             2.5
                          ],
                         ids=[
                             'integers as radius',
                             'floats as radius'
                         ])
def test_circle_perimet_posit(type_of_data):
    """Позитивные проверки метода расчета периметра Круга"""
    radius = type_of_data
    test_circle = Circle(radius)
    assert test_circle.perimeter == pi * radius * 2, 'Расчет периметра круга неверен'


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             2,
                             2.5
                          ],
                         ids=[
                             'integers as radius',
                             'floats as radius'
                         ])
def test_circle_area_posit(type_of_data):
    """Позитивные проверки метода расчета площади Круга"""
    radius = type_of_data
    test_circle = Circle(radius)
    assert test_circle.area == pi * radius ** 2, 'Расчет площади круга неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             '3',
                             True,
                             0
                          ],
                         ids=[
                             'str as radius',
                             'bool as radius',
                             'zeros as radius'
                         ])
def test_circle_creat_negot(type_of_data):
    """Негативные проверки создания объектов Круга"""
    radius = type_of_data
    with pytest.raises(ValueError):
        Circle(radius)
