from abc import ABC


class Coffee(ABC):

    def __init__(self, amount: float = 0.0):
        self.__amount = amount

    def add(self, amount: float = 0.0) -> None:
        self.__amount += amount

    def subtract(self, amount: float = 0.0) -> None:
        if amount > self.__amount:
            self.__amount = 0

        self.__amount -= amount

    def get_amount(self) -> float:
        return self.__amount
