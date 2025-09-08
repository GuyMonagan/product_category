from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Задаёт структуру и обязательные методы.
    """

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        """Сеттер цены"""
        pass
