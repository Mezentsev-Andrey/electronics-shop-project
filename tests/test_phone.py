from src.phone import Phone


def test_phone_creation():
    """
    Тестовая функция проверяющая, что при создании экземпляра класса Phone
    с указанными параметрами, соответствующие атрибуты (name, price, quantity,
    number_of_sim) присваиваются корректным значениям.
    """
    phone = Phone("Phone1", 50000, 10, 2)
    assert phone.name == "Phone1"
    assert phone.price == 50000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_phone_set_number_of_sim():
    """
    Тестовая функция для проверки установки значения
    числа SIM-карт объекта Phone.
    """
    phone = Phone("Phone1", 50000, 10, 2)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_number_of_sim_setter():
    """
    Тестовая функция для проверки сеттера числа SIM-карт объекта Phone.
    """
    phone = Phone("Phone1", 50000, 5, 2)
    try:
        phone.number_of_sim = -1
        assert False, "Expected a ValueError to be raised"
    except ValueError as error:
        assert str(error) == ('Количество физических SIM-карт'
                              ' должно быть целым числом больше нуля.')


def test_phone_str_representation():
    """
    Тестовая функция для проверки строкового представления объекта Phone.
    """
    phone = Phone("Phone1", 50000, 10, 2)
    assert str(phone) == "Phone1"


def test_phone_repr_representation():
    """
    Тестовая функция для проверки представления объекта Phone
    в виде строки для repr.
    """
    phone = Phone("Phone1", 50000, 10, 2)
    assert repr(phone) == "Phone('Phone1', 50000, 10, 2)"
