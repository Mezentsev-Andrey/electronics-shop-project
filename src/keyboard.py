from src.item import Item


class MixinLanguage:
    """
    Миксин-класс для хранения и изменения раскладки клавиатуры.
    """
    def __init__(self) -> None:
        self.__language = 'EN'

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str) -> None:
        self.__language = language

    def change_lang(self) -> None:
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, MixinLanguage):
    """
    Класс для товара "клавиатура".
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Создание экземпляра класса Keyboard."""
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
