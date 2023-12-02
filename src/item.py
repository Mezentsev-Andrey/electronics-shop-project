import csv
import math
from typing import Any


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
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

    def apply_discount(self, discount) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= 1 - discount / 100

    @classmethod
    def instantiate_from_csv(cls, file_path: Any) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла CSV.
        :param file_path: путь к CSV-файлу.
        """
        cls.all.clear()
        with open(file_path, encoding="windows-1251") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                name = row["name"]
                price = Item.string_to_number(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string: str):
        """
        Статический метод, возвращающий число из числа-строки.
        :param string: число в виде строки.
        :return: преобразованное число.
        """
        return int(math.floor(float((string.replace(",", ".")))))
