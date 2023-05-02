from abc import ABC


class Ingredient(ABC):

    def __init__(self, amount: float = 0.0) -> None:
        self.__amount = amount

    def __str__(self) -> str:
        return f'Ingredient'

    def get_amount(self) -> float:
        return self.__amount

    def increase(self, amount: float = 0.0) -> None:
        self.__amount += amount

    def decrease(self, amount: float = 0.0) -> None:
        if amount >= self.__amount:
            self.__amount = 0

        self.__amount -= amount
