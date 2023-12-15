import csv
import math
from typing import Any


class InstantiateCSVError(Exception):
    """
    Обработка исключений при повреждении файла.
    """

    def __init__(self, message) -> None:
        """
        Инициализация экземпляра класса.
        """
        self.message = message

    def __str__(self) -> str:
        """
        Вывод информации для пользователя: текст ошибки.
        """
        return f"{self.message}"


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []  # type: ignore

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self) -> str:
        """
        Геттер для получения значения приватного атрибута name.
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Сеттер для установки значения приватного атрибута name.
        Проверяет длину наименования товара и обрезает, если необходимо.
        """
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self, discount: int | float) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= 1 - discount / 100

    @classmethod
    def instantiate_from_csv(cls, file_path: str = "items.csv") -> None:
        """
        Инициализирует экземпляры класса Item данными из файла CSV.
        :param file_path: путь к CSV-файлу. По умолчанию: "items.csv"
        """
        cls.all.clear()
        try:
            with open(file_path, encoding="windows-1251") as f:
                reader = csv.DictReader(f, delimiter=",")
                # Проверка наличия нужных колонок
                required_columns = ["name", "price", "quantity"]
                if not all(column in reader.fieldnames for column in required_columns):
                    raise InstantiateCSVError("Файл item.csv поврежден")

                for row in reader:
                    name = row["name"]
                    price = cls.string_to_number(row["price"])
                    quantity = int(row["quantity"])
                    cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки.
        :param string: число в виде строки.
        :return: преобразованное число.
        """
        return int(math.floor(float((string.replace(",", ".")))))

    def __add__(self, other: Any) -> int:
        """
        Функция, для сложения атрибутов классов.
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise ValueError("Складывать можно только объекты Item и дочерние от них.")
