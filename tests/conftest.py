"""Модуль фикстур Pytest"""
import pytest


@pytest.fixture
def get_data_rectangle_positive():
    """
    Фикстура для получения данных для позитивных проверок
    объектов прямоугольника
    """
    return {
            'integer': [1, 2],
            'float': [2.5, 3.5]
            }


@pytest.fixture
def get_data_rectangle_negotive():
    """
    Фикстура для получения данных для негативных проверок
    объектов прямоугольника
    """
    return {
            'str': ['1', '2'],
            'bool': [True, True],
            'zero': [0, 0]
            }


@pytest.fixture
def get_data_triangle_positive():
    """
    Фикстура для получения данных для позитивных проверок
    объектов треугольника
    """
    return {
            'integer': [1, 3, 3],
            'float': [1.5, 3.5, 3.5]
            }


@pytest.fixture
def get_data_triangle_negotive():
    """
    Фикстура для получения данных для негативных проверок
    объектов треугольника
    """
    return {
            'str': ['1', '3', '3'],
            'bool': [True, True, True],
            'zero': [0, 0, 0],
            'inequality': [1, 2, 3]
            }


@pytest.fixture
def get_data_circle_positive():
    """
    Фикстура для получения данных для позитивных проверок
    объектов круга
    """
    return {
            'integer': 2,
            'float': 2.5
            }


@pytest.fixture
def get_data_circle_negotive():
    """
    Фикстура для получения данных для негативных проверок
    объектов круга
    """
    return {
            'str': '3',
            'bool': True,
            'zero': 0
            }


@pytest.fixture
def get_data_square_positive():
    """
    Фикстура для получения данных для позитивных проверок
    объектов квадрата
    """
    return {
            'integer': 2,
            'float': 2.5
            }


@pytest.fixture
def get_data_square_negotive():
    """
    Фикстура для получения данных для негативных проверок
    объектов квадрата
    """
    return {
            'str': '2',
            'bool': True,
            'zero': 0
            }
