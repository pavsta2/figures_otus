"""Модуль тестов класса Trangle"""
from math import sqrt
import pytest
from src.triangle import Triangle


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
def test_triangle_creat_posit(type_of_data, get_data_triangle_positive):
    """Позитивные тесты создания объектов Треугольника"""
    side_a, side_b, side_c = get_data_triangle_positive[type_of_data]
    try:
        Triangle(side_a, side_b, side_c)
    except ValueError as exc:
        assert False, (f'Создание объекта треугольника со сторонами {side_a}, {side_b}, {side_c} '
                       f'вызывает ошибку {exc}')


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
def test_triangle_perimet_posit(type_of_data, get_data_triangle_positive):
    """Позитивные тесты метода расчета периметра Треугольника"""
    side_a, side_b, side_c = get_data_triangle_positive[type_of_data]
    test_triangle = Triangle(side_a, side_b, side_c)
    assert test_triangle.perimeter == side_a + side_b + side_c, ('Расчет периметра треугольника '
                                                                 'неверен')


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
def test_triangle_area_posit(type_of_data, get_data_triangle_positive):
    """Позитивные тесты метода расчета площади Треугольника"""
    side_a, side_b, side_c = get_data_triangle_positive[type_of_data]
    test_triangle = Triangle(side_a, side_b, side_c)
    perimeter = side_a + side_b + side_c
    assert test_triangle.area == sqrt(perimeter/2 * (perimeter/2 - side_a) *
                    (perimeter/2 - side_b) * (perimeter/2 - side_c)), ('Расчет площади '
                                                                       'треугольника неверен')


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             'str',
                             'bool',
                             'zero',
                             'inequality'
                          ],
                         ids=[
                             'str as sides',
                             'bool as sides',
                             'zeros as sides',
                             'triangle inequalities rule is violated'
                         ])
def test_triangle_creat_negot(type_of_data, get_data_triangle_negotive):
    """Негативные тесты создания объектов Треугольника"""
    side_a, side_b, side_c = get_data_triangle_negotive[type_of_data]
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
