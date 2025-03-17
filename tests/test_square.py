"""Модуль тестов класса Square"""
import pytest
from src.square import Square


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
def test_square_creat_posit(type_of_data, get_data_square_positive):
    """Позитивные тесты создания объектов Квадрата"""
    side_a = get_data_square_positive[type_of_data]
    try:
        Square(side_a)
    except ValueError as exc:
        assert False, f'Создание объекта прямоугольника со стороной {side_a} вызывает ошибку {exc}'


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
def test_square_perimet_posit(type_of_data, get_data_square_positive):
    """Позитивные тесты метода расчета периметра Квадрата"""
    side_a = get_data_square_positive[type_of_data]
    test_square = Square(side_a)
    assert test_square.perimeter == (side_a) * 4, 'Расчет периметра квадрата неверен'


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
def test_square_area_posit(type_of_data, get_data_square_positive):
    """Позитивные тесты метода расчета площади Квадрата"""
    side_a = get_data_square_positive[type_of_data]
    test_square = Square(side_a)
    assert test_square.area == side_a * side_a, 'Расчет площади квадрата неверен'


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
def test_square_creat_negot(type_of_data, get_data_square_negotive):
    """Негативные тесты создания объектов Квадрата"""
    side_a = get_data_square_negotive[type_of_data]
    with pytest.raises(ValueError):
        Square(side_a)
