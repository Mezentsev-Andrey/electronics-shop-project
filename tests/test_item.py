import pytest

from src.item import Item


@pytest.fixture
def setup_items():
    """
    Фикстура предоставляющая тестам стандартный комплект данных
    для проверки методов класса.
    """
    item1 = Item("Товар1", 1000, 10)
    item2 = Item("Товар2", 5000, 50)
    return item1, item2


def test_calculate_total_price(setup_items):
    """
    Тестовая функция, которая проверяет, что общая стоимость
    рассчитывается верно.
    """
    item1, item2 = setup_items
    total_price_item1 = item1.calculate_total_price()
    total_price_item2 = item2.calculate_total_price()
    assert total_price_item1 == 1000 * 10 * 1.0  #
    assert total_price_item2 == 5000 * 50 * 1.0


def test_apply_discount(setup_items):
    """
    Тестовая функция проверяет, что скидка применена корректно.
    """
    item1, _ = setup_items
    item1.apply_discount(10)
    assert item1.price == 1000 * 0.9  #


def test_total_price_after_discount(setup_items):
    """
    Тестовая функция проверяющая, что общая стоимость после скидки
    рассчитывается верно.
    """
    item1, _ = setup_items
    item1.apply_discount(10)
    total_price_item1_after_discount = item1.calculate_total_price()
    assert total_price_item1_after_discount == 1000 * 10 * 0.9


def test_all_items_list(setup_items):
    """
    Тестовая функция, которая проверяет, что элемент был добавлен в список all.
    """
    item1, item2 = setup_items
    assert item1 in Item.all
    assert item2 in Item.all
