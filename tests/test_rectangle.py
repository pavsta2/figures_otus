"""Модуль тестов класса Rectangle"""
import pytest
from src.rectangle import Rectangle


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
def test_rectangle_creat_posit(type_of_data, get_data_rectangle_positive):
    """Позитивные тесты создания объектов Прямоугольника"""
    side_a, side_b = get_data_rectangle_positive[type_of_data]
    try:
        Rectangle(side_a, side_b)
    except ValueError as exc:
        assert False, (f'Создание объекта прямоугольника со сторонами {side_a}, {side_b} '
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
def test_rectangle_perimet_posit(type_of_data, get_data_rectangle_positive):
    """Позитивные тесты метода расчета периметра Прямоугольника"""
    side_a, side_b = get_data_rectangle_positive[type_of_data]
    test_rectangle = Rectangle(side_a, side_b)
    assert test_rectangle.perimeter == (side_a + side_b) * 2, ('Расчет периметра прямоугольника '
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
def test_rectangle_area_posit(type_of_data, get_data_rectangle_positive):
    """Позитивные тесты метода расчета площади Прямоугольника"""
    side_a, side_b = get_data_rectangle_positive[type_of_data]
    test_rectangle = Rectangle(side_a, side_b)
    assert test_rectangle.area == side_a * side_b, 'Расчет площади прямоугольника неверен'


@pytest.mark.negot
@pytest.mark.parametrize('type_of_data',
                         [
                             'str',
                             'bool',
                             'zero'
                          ],
                         ids=[
                             'str as sides',
                             'bool as sides',
                             'zeros as sides'
                         ])
def test_rectangle_creat_negot(type_of_data, get_data_rectangle_negotive):
    """Негативные тесты создания объектов Прямоугольника"""
    side_a, side_b = get_data_rectangle_negotive[type_of_data]
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
