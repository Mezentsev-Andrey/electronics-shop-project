from unittest.mock import mock_open, patch

import pytest

from src.item import InstantiateCSVError, Item


def test_item_name_setter():
    """
    Тестовая функция проверяющая длину названия товаров.
    """
    # Создаем экземпляр класса Item
    item = Item("ТестовоеИмя", 1000, 50)

    # Устанавливаем новое имя, которое должно быть обрезано
    item.name = "НовоеДлинноеИмя"
    assert item._Item__name == "НовоеДлинн"

    # Устанавливаем новое имя, которое должно быть сохранено без изменений
    item.name = "Короткое"
    assert item._Item__name == "Короткое"

    # Устанавливаем новое имя, которое должно быть обрезано до 10 символов
    item.name = "ОченьДлинноеИмяКотороеДолжноБытьОбрезано"
    assert item._Item__name == "ОченьДлинн"

    # Устанавливаем новое имя с длиной 10 символов, которое должно быть
    # сохранено без изменений
    item.name = "МоёИмяТоже"
    assert item._Item__name == "МоёИмяТоже"


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
    assert total_price_item1 == 1000 * 10 * 1.0
    assert total_price_item2 == 5000 * 50 * 1.0


def test_apply_discount(setup_items):
    """
    Тестовая функция проверяет, что скидка применена корректно.
    """
    item1, _ = setup_items
    item1.apply_discount(10)
    assert item1.price == 1000 * 0.9


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


@pytest.fixture
def sample_csv_data():
    """
    Фикстура предоставляющая тестам стандартный комплект
    данных для тестирования.
    """
    csv_data = "name,price,quantity\n" "Item1,10.5,3\n" "Item2,20.2,5\n" "Item3,5.0,2"
    return csv_data


def test_instantiate_from_csv(sample_csv_data):
    """
    Тестовая функция позволяющая удостовериться, что метод правильно
    обрабатывает CSV-файл, создавая экземпляры класса Item с правильными
    значениями атрибутов.
    """
    # Записываем временный файл с данными
    file_path = "test_data.csv"
    with open(file_path, "w") as file:
        file.write(sample_csv_data)

    # Проверяем, что метод instantiate_from_csv корректно создает
    # экземпляры класса из CSV
    Item.instantiate_from_csv(file_path)
    assert len(Item.all) == 3

    # Проверяем, что созданные экземпляры имеют правильные значения атрибутов
    assert Item.all[0].name == "Item1"
    assert Item.all[0].price == 10
    assert Item.all[0].quantity == 3

    # Проверяем, что файл очищается перед загрузкой новых данных
    Item.instantiate_from_csv(file_path)
    assert len(Item.all) == 3


def test_instantiate_from_csv_file_not_found():
    """
    Тестовая функция проверяющая, что исключение FileNotFoundError возникает при попытке
    создания экземпляра класса Item из CSV файла, который не существует.
    """
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv(file_path="nonexistent_file.csv")


def test_instantiate_from_csv_file_corrupted():
    """
    Тестовая функция проверяющая, что исключение InstantiateCSVError возникает при попытке
    создания экземпляра класса Item из CSV файла с поврежденными данными.
    """
    with patch("builtins.open", mock_open(read_data="corrupted_data")):
        with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
            Item.instantiate_from_csv(file_path="test.csv")


def test_string_to_number():
    """
    Тестовая функция проверяющая, что метод string_to_number
    корректно преобразует строки в числа.
    """
    assert Item.string_to_number("10.5") == 10
    assert Item.string_to_number("20.2") == 20
    assert Item.string_to_number("5.0") == 5


@pytest.fixture
def item():
    """
    Фикстура предоставляющая тестам стандартный комплект данных
    для проверки магических методов.
    """
    return Item("Смартфон", 10000, 20)


def test_item_creation(item):
    """
    Тестовая функция проверяющая, что при создании экземпляра класса Item
    с указанными параметрами, соответствующие атрибуты (name, price, quantity)
    присваиваются корректным значениям.
    """
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_item_repr(item):
    """
    Тестовая функция для проверки магического метода __str__
    """
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_item_str(item):
    """
    Тестовая функция для проверки магического метода __repr__
    """
    assert str(item) == "Смартфон"


def test_add_valid_objects():
    """
    Тестовая функция проверяющая корректность сложения двух
    объектов класса Item.
    """
    item1 = Item("Item1", 10000, 5)
    item2 = Item("Item2", 15000, 3)
    result = item1 + item2
    assert result == 8


def test_add_invalid_objects():
    """
    Тестовая функция проверяющая обработку ошибки при попытке
    сложения объекта класса Item с недопустимым объектом.
    """
    item1 = Item("Item1", 10000, 5)
    invalid_object = "invalid"  # Передаем недопустимый объект для сложения
    with pytest.raises(ValueError, match="Складывать можно только объекты Item и дочерние от них."):
        assert item1 + invalid_object


def test_add_different_types():
    """
    Тестовая функция проверяющая ошибки при сложении объекта Item
    с объектом другого класса.
    """
    item1 = Item("Item1", 10000, 5)

    class AnotherClass:
        quantity = 3

    item2 = AnotherClass()  # Передаем объект другого класса
    with pytest.raises(ValueError, match="Складывать можно только объекты Item и дочерние от них."):
        assert item1 + item2
