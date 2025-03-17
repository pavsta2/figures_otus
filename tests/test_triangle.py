"""Модуль тестов класса Trangle"""
from math import sqrt
import pytest
from src.triangle import Triangle


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 3, 3],
                             [1.5, 3.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_triangle_creat_posit(type_of_data):
    """Позитивные тесты создания объектов Треугольника"""
    side_a, side_b, side_c = type_of_data
    assert Triangle(side_a, side_b, side_c)


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 3, 3],
                             [1.5, 3.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_triangle_perimet_posit(type_of_data):
    """Позитивные тесты метода расчета периметра Треугольника"""
    side_a, side_b, side_c = type_of_data
    test_triangle = Triangle(side_a, side_b, side_c)
    assert test_triangle.perimeter == side_a + side_b + side_c, ('Расчет периметра треугольника '
                                                                 'неверен')


@pytest.mark.posit
@pytest.mark.parametrize('type_of_data',
                         [
                             [1, 3, 3],
                             [1.5, 3.5, 3.5]
                          ],
                         ids=[
                             'integers as sides',
                             'floats as sides'
                         ])
def test_triangle_area_posit(type_of_data):
    """Позитивные тесты метода расчета площади Треугольника"""
    side_a, side_b, side_c = type_of_data
    test_triangle = Triangle(side_a, side_b, side_c)
    perimeter = side_a + side_b + side_c
    assert test_triangle.area == sqrt(perimeter/2 * (perimeter/2 - side_a) *
                    (perimeter/2 - side_b) * (perimeter/2 - side_c)), ('Расчет площади '
                                                                       'треугольника неверен')


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             ['1', '3', '3'],
                             [True, True, True],
                             [0, 0, 0],
                             [1, 2, 3]
                          ],
                         ids=[
                             'str as sides',
                             'bool as sides',
                             'zeros as sides',
                             'triangle inequalities rule is violated'
                         ])
def test_triangle_creat_negot(type_of_data):
    """Негативные тесты создания объектов Треугольника"""
    side_a, side_b, side_c = type_of_data
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
